# init(handle:nameComponents:contactIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a person object with the specified display name and contact information.

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(handle: String, nameComponents: PersonNameComponents, contactIdentifier: String?)
```

```objc
- (instancetype) initWithHandle:(NSString *) handle nameComponents:(NSPersonNameComponents *) nameComponents contactIdentifier:(NSString *) contactIdentifier;
```

## Return Value

An initialized person object or `nil` if the object could not be created.

## Discussion

Use this method as a convenient way to create person objects that do not require an image.

## Parameters

- `handle`: A string containing information that your app uses to identify the user. You can use an email address, phone number, account name, or any information that lets you identify the user uniquely.
- `nameComponents`: The name of the user, specified as a set of name components.
- `contactIdentifier`: The identifier associated with the user’s [`CNContact`](../../Contacts/cncontact.md) object. Specify a value for this parameter when the user has a corresponding entry in the Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/init(handle:namecomponents:contactidentifier:))*