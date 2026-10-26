# init(personHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a person with the specified name and contact information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?)
```

```objc
- (instancetype) initWithPersonHandle:(INPersonHandle *) personHandle nameComponents:(NSPersonNameComponents *) nameComponents displayName:(NSString *) displayName image:(INImage *) image contactIdentifier:(NSString *) contactIdentifier customIdentifier:(NSString *) customIdentifier;
```

#### Return Value

An initialized person object or `nil` if initialization fails.

#### Discussion

Use this method when creating person objects you plan to return as part of a response to Siri. Always specify as much information as possible about the user. This method makes copies of the `personHandle`, `nameComponents`, `displayName`, `image`, `contactIdentifier`, and `customIdentifier` parameters instead of keeping the originals.

## Parameters

- `personHandle`: A string that contains information your app uses to identify the user. You can create a person handle from an email address, phone number, or account name associated with the user.
- `nameComponents`: The name of the user, specified as a set of name components.
- `displayName`: The string you display for the user’s name.
- `image`: An image of the person.
- `contactIdentifier`: The identifier associated with the user’s [`CNContact`](../../Contacts/cncontact.md) object. Specify a value for this parameter when the user has a corresponding entry in the Contacts database.
- `customIdentifier`: A custom string that you use to identify people in your app.

## See Also

### Creating a person
- [init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme%29.md)
  Creates a person with information that indicates whether the person is the user of the device.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, relationship: INPersonRelationship?)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,relationship%29.md)
  Creates a person with the specified name, contact, and relationship information.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme,suggestiontype%29.md)
  Creates a person that includes required metadata for messaging intents.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, aliases: [INPersonHandle]?, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,aliases,suggestiontype%29.md)
  Creates a person with the specified name, contact, and alias information.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isContactSuggestion: Bool, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,iscontactsuggestion,suggestiontype%29.md)
  Creates a person with information Siri can use to suggestion the person at appropriate times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/init(personhandle:namecomponents:displayname:image:contactidentifier:customidentifier:))*