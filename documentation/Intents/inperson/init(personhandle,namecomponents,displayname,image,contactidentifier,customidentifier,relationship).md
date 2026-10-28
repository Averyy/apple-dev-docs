# init(personHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:relationship:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a person with the specified name, contact, and relationship information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, relationship: INPersonRelationship?)
```

```objc
- (instancetype) initWithPersonHandle:(INPersonHandle *) personHandle nameComponents:(NSPersonNameComponents *) nameComponents displayName:(NSString *) displayName image:(INImage *) image contactIdentifier:(NSString *) contactIdentifier customIdentifier:(NSString *) customIdentifier relationship:(INPersonRelationship) relationship;
```

## Return Value

An initialized person object or `nil` if initialization fails.

## Discussion

Use this method when creating person objects you plan to return as part of a response to Siri. Specify as much information as possible about the user. This method makes copies of the parameters instead of keeping the originals.

## Parameters

- `personHandle`: A string that contains information your app uses to identify the user. You can create a person handle from an email address, phone number, or account name associated with the user.
- `nameComponents`: The name of the user, specified as a set of name components.
- `displayName`: The string you display for the user’s name.
- `image`: An image of the person.
- `contactIdentifier`: The identifier associated with the user’s [`CNContact`](../../Contacts/cncontact.md) object. Specify a value for this parameter when the user has a corresponding entry in the Contacts database.
- `customIdentifier`: A custom string that you use to identify people in your app.
- `relationship`: The relationship of this person to the current user.

## See Also

### Creating a person
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier%29.md)
  Creates a person with the specified name and contact information.
- [init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme%29.md)
  Creates a person with information that indicates whether the person is the user of the device.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme,suggestiontype%29.md)
  Creates a person that includes required metadata for messaging intents.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, aliases: [INPersonHandle]?, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,aliases,suggestiontype%29.md)
  Creates a person with the specified name, contact, and alias information.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isContactSuggestion: Bool, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,iscontactsuggestion,suggestiontype%29.md)
  Creates a person with information Siri can use to suggestion the person at appropriate times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/init(personhandle:namecomponents:displayname:image:contactidentifier:customidentifier:relationship:))*