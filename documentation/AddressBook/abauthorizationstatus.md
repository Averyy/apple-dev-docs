# ABAuthorizationStatus

**Framework**: Address Book  
**Kind**: enum  
**Role**: Enumeration

Different possible values for the authorization status of an app with respect to address book data.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: use CNAuthorizationStatus

## Declaration

```swift
enum ABAuthorizationStatus
```

```c
enum ABAuthorizationStatus : CFIndex;
```

## Topics

### Constants
- [ABAuthorizationStatus.notDetermined](./abauthorizationstatus/notdetermined.md)
  No authorization status could be determined.
- [ABAuthorizationStatus.restricted](./abauthorizationstatus/restricted.md)
  The app is not authorized to access address book data. The user cannot change this access, possibly due to restrictions such as parental controls.
- [ABAuthorizationStatus.denied](./abauthorizationstatus/denied.md)
  The user explicitly denied access to address book data for this app.
- [ABAuthorizationStatus.authorized](./abauthorizationstatus/authorized.md)
  The app is authorized to access address book data.
### Initializers
- [init?(rawValue: CFIndex)](./abauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [struct ABPersonImageFormat](./abpersonimageformat.md)
  Indicates an image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abauthorizationstatus)*