# init(personHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:isContactSuggestion:suggestionType:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a person with information Siri can use to suggestion the person at appropriate times.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isContactSuggestion: Bool, suggestionType: INPersonSuggestionType)
```

```objc
- (instancetype) initWithPersonHandle:(INPersonHandle *) personHandle nameComponents:(NSPersonNameComponents *) nameComponents displayName:(NSString *) displayName image:(INImage *) image contactIdentifier:(NSString *) contactIdentifier customIdentifier:(NSString *) customIdentifier isContactSuggestion:(BOOL) isContactSuggestion suggestionType:(INPersonSuggestionType) suggestionType;
```

## See Also

### Creating a person
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier%29.md)
  Creates a person with the specified name and contact information.
- [init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme%29.md)
  Creates a person with information that indicates whether the person is the user of the device.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, relationship: INPersonRelationship?)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,relationship%29.md)
  Creates a person with the specified name, contact, and relationship information.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, isMe: Bool, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme,suggestiontype%29.md)
  Creates a person that includes required metadata for messaging intents.
- [convenience init(personHandle: INPersonHandle, nameComponents: PersonNameComponents?, displayName: String?, image: INImage?, contactIdentifier: String?, customIdentifier: String?, aliases: [INPersonHandle]?, suggestionType: INPersonSuggestionType)](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,aliases,suggestiontype%29.md)
  Creates a person with the specified name, contact, and alias information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/init(personhandle:namecomponents:displayname:image:contactidentifier:customidentifier:iscontactsuggestion:suggestiontype:))*