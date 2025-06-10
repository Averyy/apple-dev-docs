# ABAuthorizationStatus

**Framework**: Address Book  
**Kind**: enum

Different possible values for the authorization status of an app with respect to address book data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum ABAuthorizationStatus
```

## Topics

### Constants
- [ABAuthorizationStatus.notDetermined](abauthorizationstatus/notdetermined.md)
  No authorization status could be determined.
- [ABAuthorizationStatus.restricted](abauthorizationstatus/restricted.md)
  The app is not authorized to access address book data. The user cannot change this access, possibly due to restrictions such as parental controls.
- [ABAuthorizationStatus.denied](abauthorizationstatus/denied.md)
  The user explicitly denied access to address book data for this app.
- [ABAuthorizationStatus.authorized](abauthorizationstatus/authorized.md)
  The app is authorized to access address book data.
### Initializers
- [init?(rawValue: CFIndex)](abauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ABPersonImageFormat](abpersonimageformat.md)
  Indicates an image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abauthorizationstatus)*