# INPerson

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Information about a person participating in a SiriKit interaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPerson
```

```objc
@interface INPerson : NSObject
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)
- [Handling an Intent](../SiriKit/handling-an-intent.md)
- [Resolving the Parameters of an Intent](../SiriKit/resolving-the-parameters-of-an-intent.md)

## Overview

SiriKit uses [`INPerson`](./inperson.md) objects to represent people with many different roles, including the sender or recipient of calls and messages, the payer or payee of a financial transaction, or the driver of a vehicle. You also use person objects to identify the corresponding contact in your app and to communicate information about that contact back to SiriKit.

When resolving the parameters of an intent, use any provided [`INPerson`](./inperson.md) objects to identify the corresponding contacts in your app. A person object contains information provided by the initial request, which could be as little as a single name spoken by the person interacting with Siri. After identifying the contact, create a new [`INPerson`](./inperson.md) object and fill it with the information that you need to identify that contact again later. For example, you might specify a value for [`personHandle`](./inperson/personhandle.md) property that contains the information about how your app identifies that contact.

When resolving the identities of contacts, SiriKit leverages the information in the device owner’s contacts database when that information is available. If the owner denies your app access to their contacts, SiriKit can’t use that information, which might cause many properties of a person object to be `nil`. Because the [`INPerson`](./inperson.md) class conforms to the [`INSpeakable`](./inspeakable.md) protocol, though, SiriKit still populates the [`spokenPhrase`](./inspeakable/spokenphrase.md) property with what the person interacting with Siri said, and you can use that information to try to identify the contact. For more information about that protocol, see [`INSpeakable`](./inspeakable.md).

> ❗ **Important**:  To provide the best experience, especially when donating instances of [`INSendMessageIntent`](./insendmessageintent.md) and [`INStartCallIntent`](./instartcallintent.md), assign a value to a person’s [`contactIdentifier`](./inperson/contactidentifier.md) if they exist in the device owner’s contacts database. Otherwise, assign a value to the [`customIdentifier`](./inperson/customidentifier.md) property that identifies the person in your app. When attempting to resolve a message recipient or call contact, prefer to use the people Siri adds to the [`siriMatches`](./inperson/sirimatches.md) property.

## Topics

### Creating a person
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?)](./inperson/init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier%29.md)
  Creates a person with the specified name and contact information.
- [init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool)](./inperson/init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme%29.md)
  Creates a person with information that indicates whether the person is the user of the device.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, relationship: INPersonRelationship?)](./inperson/init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,relationship%29.md)
  Creates a person with the specified name, contact, and relationship information.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool, suggestionType: INPersonSuggestionType)](./inperson/init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme,suggestiontype%29.md)
  Creates a person that includes required metadata for messaging intents.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, aliases: [INPersonHandle]?, suggestionType: INPersonSuggestionType)](./inperson/init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,aliases,suggestiontype%29.md)
  Creates a person with the specified name, contact, and alias information.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isContactSuggestion: Bool, suggestionType: INPersonSuggestionType)](./inperson/init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,iscontactsuggestion,suggestiontype%29.md)
  Creates a person with information Siri can use to suggestion the person at appropriate times.
### Accessing the name
- [var displayName: String](./inperson/displayname.md)
  The person’s formatted name.
- [var nameComponents: PersonNameComponents?](./inperson/namecomponents.md)
  The individual components of the person’s full name.
### Accessing the person’s identity
- [var personHandle: INPersonHandle?](./inperson/personhandle.md)
  The unique handle that your app assigns to the person.
- [var image: INImage?](./inperson/image.md)
  An image of the person.
- [var isMe: Bool](./inperson/isme.md)
  A Boolean value indicating whether the person is the user of the device.
- [var aliases: [INPersonHandle]?](./inperson/aliases.md)
  The additional handles that Siri may use to identify the person.
### Accessing app-specific identifiers
- [var contactIdentifier: String?](./inperson/contactidentifier.md)
  The Contacts database identifier for the person.
- [var customIdentifier: String?](./inperson/customidentifier.md)
  The unique identifier that your app uses to identify the person.
### Accessing suggestion details
- [var isContactSuggestion: Bool](./inperson/iscontactsuggestion.md)
  A Boolean value that indicates whether the person is a contact suggestion.
- [var suggestionType: INPersonSuggestionType](./inperson/suggestiontype.md)
  The type of contact information to donate with interactions.
- [enum INPersonSuggestionType](./inpersonsuggestiontype.md)
  Constants indicating how to display the person’s identity.
### Accessing relationship details
- [var relationship: INPersonRelationship?](./inperson/relationship.md)
  The relationship between this person and the person using the device.
- [struct INPersonRelationship](./inpersonrelationship.md)
  Constants indicating the relationship between the person using the device and another person.
### Accessing matched people
- [var siriMatches: [INPerson]?](./inperson/sirimatches.md)
  The list of matches Siri provides for you to resolve or disambiguate.
### Deprecated
- [Deprecated Symbols](../SiriKit/deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Initializers
- [init?(coder: NSCoder)](./inperson/init%28coder%29.md)
- [convenience init(handle: String, displayName: String?, contactIdentifier: String?)](./inperson/init%28handle,displayname,contactidentifier%29.md)
  Creates a person object with the specified display name and contact information.
- [convenience init(handle: String, nameComponents: PersonNameComponents, contactIdentifier: String?)](./inperson/init%28handle,namecomponents,contactidentifier%29.md)
  Creates a person object with the specified display name and contact information.
- [convenience init(handle: String, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?)](./inperson/init%28handle,namecomponents,displayname,image,contactidentifier%29.md)
  Creates a person object with the specified name and contact information.
### Instance Properties
- [var handle: String?](./inperson/handle.md)
  The unique identifier that your app assigned to the user.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [INRestaurantGuest](./inrestaurantguest.md)
- [INRideDriver](./inridedriver.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [INSpeakable](./inspeakable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Contacts
- [class INPersonHandle](./inpersonhandle.md)
  The identifying information for a user of your app.
- [struct INPersonHandleLabel](./inpersonhandlelabel.md)
  Constants describing how the person handle relates to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson)*