# TN3149: Fetching Contacts change history events

**Framework**: Technotes  
**Role**: Technote

Learn how to fetch and process the most recent changes to the Contacts database.

## Overview

The Contacts framework has a new fetch request to retrieve information from the user’s Contacts database. A change history fetch request efficiently returns a collection of change history events that describes the contacts and groups added to, deleted from, and updated in the Contacts database. You can fetch all changes in the database or limit the search to changes that have occurred since your last fetch operation. Then, inspect the fetch result to determine what changes have occurred such as a contact was updated or a contact was removed from a group. To fetch change history events in your app, follow these steps:

1. Adopt the change history event visitor protocol.
2. Create a change history fetch request.
3. Configure the change history fetch request
4. Execute the change history fetch request.
5. Process a change history event.
6. Save the starting history token.

> ❗ **Important**: Your app needs to obtain permission from the user before accessing Contacts entries. See [Requesting Authorization to Access Contacts](../Contacts/accessing-the-contact-store.md) for details.

## Adopt the change history event visitor protocol

The [CNChangeHistoryEvent](../Contacts/cnchangehistoryevent.md) class encapsulates all possible changes that the system can make to the Contacts database, such as dropping cached information, adding a contact, or updating a group. To receive these changes in your app, create and use a class that conforms to the [CNChangeHistoryEventVisitor](../Contacts/cnchangehistoryeventvisitor.md) protocol. Classes adopting this protocol must implement the [visitDropEverythingEvent:](../Contacts/cnchangehistoryeventvisitor/visit%28_%29-2yhz3.md), [visitAddContactEvent:](../Contacts/cnchangehistoryeventvisitor/visit%28_%29-9w73y.md), [visitUpdateContactEvent:](../Contacts/cnchangehistoryeventvisitor/visit%28_%29-1pf2a.md), and [visitDeleteContactEvent:](../Contacts/cnchangehistoryeventvisitor/visit%28_%29-ci4z.md) instance methods.

```objc
@interface MyEventVisitor : NSObject <CNChangeHistoryEventVisitor>
@end

@implementation MyEventVisitor
// Drop all cached information.
- (void)visitDropEverythingEvent:(CNChangeHistoryDropEverythingEvent *)event {
      NSLog(@"Received a drop everything event.");
}

// The user added a contact to the database.
- (void)visitAddContactEvent:(CNChangeHistoryAddContactEvent *)event {
      NSLog(@"The user added a contact with family name, %@, to their account with identifier %@.",event.contact.familyName, event.containerIdentifier);
}

// The user updated a contact in the database.
- (void)visitUpdateContactEvent:(CNChangeHistoryUpdateContactEvent *)event {
     NSLog(@"The user updated the contact with family name, %@.",event.contact.familyName);
}

// The user removed a contact from the database.
- (void)visitDeleteContactEvent:(CNChangeHistoryDeleteContactEvent *)event {
      NSLog(@"The user removed the contact identified by %@ from the database.",event.contactIdentifier);
}
@end
```

[`CNChangeHistoryEventVisitor`](../Contacts/cnchangehistoryeventvisitor.md) also provides optional methods such as [visitAddMemberToGroupEvent:](../Contacts/cnchangehistoryeventvisitor/visitaddmember%28_%29.md). Each method provides the change history event associated with the changes. Inspect the properties of the event to detemine the new values or modifications brought to contact properties. For example, [`visitUpdateContactEvent:`](../Contacts/cnchangehistoryeventvisitor/visit%28_%29-1pf2a.md) provides a [CNChangeHistoryUpdateContactEvent](../Contacts/cnchangehistoryupdatecontactevent.md) object whose [contact](../Contacts/cnchangehistoryupdatecontactevent/contact.md) instance property contains updated information about an existing contact. Compare [`contact`](../Contacts/cnchangehistoryupdatecontactevent/contact.md) to your app’s cached contact properties to determine what properties were updated.

## Create a change history fetch request

Call [CNChangeHistoryFetchRequest](../Contacts/cnchangehistoryfetchrequest.md) to create a change history fetch request.

```objc
CNChangeHistoryFetchRequest *fetchRequest = [[CNChangeHistoryFetchRequest alloc] init];
```

The change history fetch request can be configured to fetch a range of change events that have occurred to the Contacts database. The range of events begins with a starting history token, [startingToken](../Contacts/cnchangehistoryfetchrequest/startingtoken.md), and ends with the current state of the database. This starting token has a default value of `nil`. If you provide an existing starting token from a previous change history fetch, the request only returns changes that occurred in history after this token.

```objc
@property (nonatomic, copy) NSData *historyToken;

self.historyToken = nil;
fetchRequest.startingToken = self.historyToken;
```

If your token has a `nil` value, is invalid or expired, the fetch request returns a drop event followed by an add event for every contact and group in the Contacts database. The drop event indicates that apps should drop cached information. The token can be persisted between the app launches on the current device.

## Configure a change history fetch request

Each [`CNChangeHistoryFetchRequest`](../Contacts/cnchangehistoryfetchrequest.md) object comes with default values that can affect the result of the operation. [`CNChangeHistoryFetchRequest`](../Contacts/cnchangehistoryfetchrequest.md) provides several properties to update these default values.

The fetch request always returns changes to contacts. Changes to groups are optional. If you want to also fetch group changes, set [includeGroupChanges](../Contacts/cnchangehistoryfetchrequest/includegroupchanges.md) to `YES`. This property indicates whether to add group changes to the fetch result. The default value is `NO`.

```objc
fetchRequest.includeGroupChanges = YES;
```

The fetch request returns immutable [CNContact](../Contacts/cncontact.md) and [CNGroup](../Contacts/cngroup.md) objects. To fetch mutable contact and group objects, set [mutableObjects](../Contacts/cnchangehistoryfetchrequest/mutableobjects.md) to `YES`. This property indicates whether to return mutable objects. The default value is `NO`.

```objc
fetchRequest.mutableObjects = YES;
```

The fetch request returns contact changes as unified contacts. A unified contact is a synthesized merged result of contacts from different accounts that represent the same person. To fetch individual contact changes, set [shouldUnifyResults](../Contacts/cnchangehistoryfetchrequest/shouldunifyresults.md) to `NO`. This property specifies whether to return contact changes for either unified contacts or individual contacts. The default value is `YES`.

```objc
fetchRequest.shouldUnifyResults = NO;
```

The Contacts framework limits the contact properties that you fetch to the unique identifier when executing a change history fetch request. The request always and primarily returns the [CNContactIdentifierKey](../Contacts/cncontactidentifierkey.md) key. To fetch additional contact properties, update [additionalContactKeyDescriptors](../Contacts/cnchangehistoryfetchrequest/additionalcontactkeydescriptors.md) with contact keys. This property takes an array of key descriptors, [CNKeyDescriptor](../Contacts/contact-keys.md). For example, if you want to fetch the email addresses and family name of contacts in addition to their unique identifiers, add the [CNContactEmailAddressesKey](../Contacts/cncontactfamilynamekey.md) and [`CNContactFamilyNameKey`](../Contacts/cncontactfamilynamekey.md) keys to [`additionalContactKeyDescriptors`](../Contacts/cnchangehistoryfetchrequest/additionalcontactkeydescriptors.md) .

```objc
fetchRequest.additionalContactKeyDescriptors = @[CNContactEmailAddressesKey, CNContactFamilyNameKey];
```

A transaction author, [transactionAuthor](../Contacts/cnsaverequest/transactionauthor.md), is a string that you provide to identify the author who performs a save request. Transaction authors use reverse-domain-style notation. We recommend using your app’s bundle identifier as the transaction author when your app is saving changes to Contacts.

```objc
CNSaveRequest *saveRequest = [[CNSaveRequest alloc] init];
saveRequest.transactionAuthor = @"com.mycompany.myappname";
```

You can later filter that author from fetched change history events. The fetch result won’t include changes made by authors you would like to ignore or exclude. To exclude changes made by certain authors, update [excludedTransactionAuthors](../Contacts/cnchangehistoryfetchrequest/excludedtransactionauthors.md) with these authors.

```objc
fetchRequest.excludedTransactionAuthors = @[@"com.mycompany.myappname"];
```

> **Note**: Transaction authors allow you to filter transactions returned in the fetched change history events. They don’t provide any information about the author responsible for making a given change.

## Execute the change history fetch request

Call [enumeratorForChangeHistoryFetchRequest:error:](../Contacts/cncontactstore/api-3294190-enumeratorforchangehistoryfetchr.md) on an instance of [CNContactStore](../Contacts/cncontactstore.md) to execute the change history fetch request. Pass the created [`CNChangeHistoryFetchRequest`](../Contacts/cnchangehistoryfetchrequest.md) object and a [NSError](../Foundation/nserror.md) object to the call.

```objc
NSError *error = nil;
// This method is unavailable in Swift.
CNFetchResult<NSEnumerator<CNChangeHistoryEvent *> *> *fetchResult = [self.store enumeratorForChangeHistoryFetchRequest:fetchRequest error:&error];
```

If the fetch request succeeds, [`enumeratorForChangeHistoryFetchRequest:error:`](../Contacts/cncontactstore/api-3294190-enumeratorforchangehistoryfetchr.md) returns a [CNFetchResult](../Contacts/cnfetchresult.md) object. Process the change history events returned in the [value](../Contacts/cnfetchresult/value.md) property of [`CNFetchResult`](../Contacts/cnfetchresult.md). If the fetch request fails, [`enumeratorForChangeHistoryFetchRequest:error:`](../Contacts/cncontactstore/api-3294190-enumeratorforchangehistoryfetchr.md) returns `nil`.

## Process a change history event

To process a change history event, call [acceptEventVisitor:](../Contacts/cnchangehistoryevent/accept%28_%29.md) on an instance of a class that conforms to [`CNChangeHistoryEventVisitor`](../Contacts/cnchangehistoryeventvisitor.md).

```objc
MyEventVisitor *myEventVisitor = [[MyEventVisitor alloc] init];
for (CNChangeHistoryEvent *event in fetchResult.value) {
    [event acceptVisitor:myEventVisitor];
}
```

If your app receives a drop everything event, enough has changed since the last time your app fetched the history changes that an incremental sync is no longer possible. Following the drop everything event, your app receives an add event for each contact and group currently in the database. This allows you to implement full syncs and incremental syncs using the same code.

> ❗ **Important**: Using [isKindOfClass](../ObjectiveC/nsobjectprotocol/iskind%28of%29.md) to determine the specific class of a change history event isn’t recommended. Use the protocol instance methods as described in [Adopt the change history event visitor protocol](./tn3149-fetching-change-history-events.md#Adopt-the-change-history-event-visitor-protocol).

## Save the starting history token

If the fetch request succeeds, inspect the [currentHistoryToken](../Contacts/cncontactstore/currenthistorytoken.md) property of [`CNFetchResult`](../Contacts/cnfetchresult.md). This property provides the history token for the current fetch request. Your app should save this token, then use it when fetching the next change history events.

```objc
self.historyToken = fetchResult.currentHistoryToken; 
```

## Revision History

- **2023-06-06** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3149-fetching-change-history-events)*