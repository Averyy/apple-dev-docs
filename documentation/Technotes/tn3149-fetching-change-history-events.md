# TN3149: Fetching Contacts change history events

**Framework**: Technotes

Learn how to fetch and process the most recent changes to the Contacts database.

#### Overview

The Contacts framework has a new fetch request to retrieve information from the user’s Contacts database. A change history fetch request efficiently returns a collection of change history events that describes the contacts and groups added to, deleted from, and updated in the Contacts database. You can fetch all changes in the database or limit the search to changes that have occurred since your last fetch operation. Then, inspect the fetch result to determine what changes have occurred such as a contact was updated or a contact was removed from a group. To fetch change history events in your app, follow these steps:

1. Adopt the change history event visitor protocol.
2. Create a change history fetch request.
3. Configure the change history fetch request
4. Execute the change history fetch request.
5. Process a change history event.
6. Save the starting history token.

> ❗ **Important**: Your app needs to obtain permission from the user before accessing Contacts entries. See [`Requesting Authorization to Access Contacts`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/requesting_authorization_to_access_contacts) for details.

#### Adopt the Change History Event Visitor Protocol

The [`CNChangeHistoryEvent`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryevent?language=objc) class encapsulates all possible changes that the system can make to the Contacts database, such as dropping cached information, adding a contact, or updating a group. To receive these changes in your app, create and use a class that conforms to the [`CNChangeHistoryEventVisitor`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor?language=objc) protocol. Classes adopting this protocol must implement the [`visitDropEverythingEvent:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/3113275-visitdropeverythingevent), [`visitAddContactEvent:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/3113269-visitaddcontactevent/), [`visitUpdateContactEvent:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/3113278-visitupdatecontactevent), and [`visitDeleteContactEvent:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/3113273-visitdeletecontactevent) instance methods.

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

[`CNChangeHistoryEventVisitor`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor?language=objc) also provides optional methods such as [`visitAddMemberToGroupEvent:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/3113271-visitaddmembertogroupevent). Each method provides the change history event associated with the changes. Inspect the properties of the event to detemine the new values or modifications brought to contact properties. For example, [`visitUpdateContactEvent:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/3113278-visitupdatecontactevent) provides a [`CNChangeHistoryUpdateContactEvent`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryupdatecontactevent?language=objc) object whose [`contact`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryupdatecontactevent/3113287-contact?language=objc) instance property contains updated information about an existing contact. Compare [`contact`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryupdatecontactevent/3113287-contact?language=objc) to your app’s cached contact properties to determine what properties were updated.

#### Create a Change History Fetch Request

Call [`CNChangeHistoryFetchRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest?language=objc) to create a change history fetch request.

```objc
CNChangeHistoryFetchRequest *fetchRequest = [[CNChangeHistoryFetchRequest alloc] init];
```

The change history fetch request can be configured to fetch a range of change events that have occurred to the Contacts database. The range of events begins with a starting history token, [`startingToken`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/3294189-startingtoken?language=objc), and ends with the current state of the database. This starting token has a default value of `nil`. If you provide an existing starting token from a previous change history fetch, the request only returns changes that occurred in history after this token.

```objc
@property (nonatomic, copy) NSData *historyToken;

self.historyToken = nil;
fetchRequest.startingToken = self.historyToken;
```

If your token has a `nil` value, is invalid or expired, the fetch request returns a drop event followed by an add event for every contact and group in the Contacts database. The drop event indicates that apps should drop cached information. The token can be persisted between the app launches on the current device.

#### Configure a Change History Fetch Request

Each [`CNChangeHistoryFetchRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest?language=objc) object comes with default values that can affect the result of the operation. [`CNChangeHistoryFetchRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest?language=objc) provides several properties to update these default values.

The fetch request always returns changes to contacts. Changes to groups are optional. If you want to also fetch group changes, set [`includeGroupChanges`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/3294186-includegroupchanges?language=objc) to `YES`. This property indicates whether to add group changes to the fetch result. The default value is `NO`.

```objc
fetchRequest.includeGroupChanges = YES;
```

The fetch request returns immutable [`CNContact`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontact?language=objc) and [`CNGroup`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cngroup?language=objc) objects. To fetch mutable contact and group objects, set [`mutableObjects`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/3294187-mutableobjects?language=objc) to `YES`. This property indicates whether to return mutable objects. The default value is `NO`.

```objc
fetchRequest.mutableObjects = YES;
```

The fetch request returns contact changes as unified contacts. A unified contact is a synthesized merged result of contacts from different accounts that represent the same person. To fetch individual contact changes, set [`shouldUnifyResults`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/3294188-shouldunifyresults?language=objc) to `NO`. This property specifies whether to return contact changes for either unified contacts or individual contacts. The default value is `YES`.

```objc
fetchRequest.shouldUnifyResults = NO;
```

The Contacts framework limits the contact properties that you fetch to the unique identifier when executing a change history fetch request. The request always and primarily returns the [`CNContactIdentifierKey`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactidentifierkey?language=objc) key. To fetch additional contact properties, update [`additionalContactKeyDescriptors`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/3294184-additionalcontactkeydescriptors?language=objc) with contact keys. This property takes an array of key descriptors, [`CNKeyDescriptor`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/contact_keys). For example, if you want to fetch the email addresses and family name of contacts in addition to their unique identifiers, add the [`CNContactEmailAddressesKey`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactfamilynamekey?language=objc) and [`CNContactEmailAddressesKey`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactfamilynamekey?language=objc) keys to [`additionalContactKeyDescriptors`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/3294184-additionalcontactkeydescriptors?language=objc) .

```objc
fetchRequest.additionalContactKeyDescriptors = @[CNContactEmailAddressesKey, CNContactFamilyNameKey];
```

A transaction author, [`transactionAuthor`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnsaverequest/3824780-transactionauthor?language=objc), is a string that you provide to identify the author who performs a save request. Transaction authors use reverse-domain-style notation. We recommend using your app’s bundle identifier as the transaction author when your app is saving changes to Contacts.

```objc
CNSaveRequest *saveRequest = [[CNSaveRequest alloc] init];
saveRequest.transactionAuthor = @"com.mycompany.myappname";
```

You can later filter that author from fetched change history events. The fetch result won’t include changes made by authors you would like to ignore or exclude. To exclude changes made by certain authors, update [`excludedTransactionAuthors`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/3294185-excludedtransactionauthors?language=objc) with these authors.

```objc
fetchRequest.excludedTransactionAuthors = @[@"com.mycompany.myappname"];
```

> **Note**: Transaction authors allow you to filter transactions returned in the fetched change history events. They don’t provide any information about the author responsible for making a given change.

#### Execute the Change History Fetch Request

Call [`enumeratorForChangeHistoryFetchRequest:error:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactstore/3294190-enumeratorforchangehistoryfetchr?language=occ) on an instance of [`CNContactStore`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactstore?language=objc) to execute the change history fetch request. Pass the created [`CNChangeHistoryFetchRequest`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest?language=objc) object and a [`NSError`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/nserror?language=occ) object to the call.

```objc
NSError *error = nil;
// This method is unavailable in Swift.
CNFetchResult<NSEnumerator<CNChangeHistoryEvent *> *> *fetchResult = [self.store enumeratorForChangeHistoryFetchRequest:fetchRequest error:&error];
```

If the fetch request succeeds, [`enumeratorForChangeHistoryFetchRequest:error:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactstore/3294190-enumeratorforchangehistoryfetchr?language=occ) returns a [`CNFetchResult`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnfetchresult?language=objc) object. Process the change history events returned in the [`value`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnfetchresult/3294194-value?language=objc) property of [`CNFetchResult`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnfetchresult?language=objc). If the fetch request fails, [`enumeratorForChangeHistoryFetchRequest:error:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactstore/3294190-enumeratorforchangehistoryfetchr?language=occ) returns `nil`.

#### Process a Change History Event

To process a change history event, call [`acceptEventVisitor:`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryevent/3113267-accepteventvisitor/) on an instance of a class that conforms to [`CNChangeHistoryEventVisitor`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor?language=objc).

```objc
MyEventVisitor *myEventVisitor = [[MyEventVisitor alloc] init];
for (CNChangeHistoryEvent *event in fetchResult.value) {
    [event acceptVisitor:myEventVisitor];
}
```

If your app receives a drop everything event, enough has changed since the last time your app fetched the history changes that an incremental sync is no longer possible. Following the drop everything event, your app receives an add event for each contact and group currently in the database. This allows you to implement full syncs and incremental syncs using the same code.

> ❗ **Important**: Using [`isKindOfClass`](https://developer.apple.comhttps://developer.apple.com/documentation/objectivec/1418956-nsobject/1418511-iskindofclass/) to determine the specific class of a change history event isn’t recommended. Use the protocol instance methods as described in [`Adopt the change history event visitor protocol`](tn3149-fetching-change-history-events#Adopt-the-change-history-event-visitor-protocol.md).

#### Save the Starting History Token

If the fetch request succeeds, inspect the [`currentHistoryToken`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cncontactstore/3113739-currenthistorytoken/) property of [`CNFetchResult`](https://developer.apple.comhttps://developer.apple.com/documentation/contacts/cnfetchresult?language=objc). This property provides the history token for the current fetch request. Your app should save this token, then use it when fetching the next change history events.

```objc
self.historyToken = fetchResult.currentHistoryToken; 
```

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3149-fetching-change-history-events)*