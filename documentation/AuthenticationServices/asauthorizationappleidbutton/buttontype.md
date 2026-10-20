# ASAuthorizationAppleIDButton.ButtonType

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

A type for the authorization button.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum ButtonType
```

```c
enum ASAuthorizationAppleIDButtonType : NSInteger;
```

## Topics

### Choosing a Button Type
- [ASAuthorizationAppleIDButton.ButtonType.continue](./buttontype/continue.md)
  A button type that continues the Sign in with Apple authorization process.
- [static var `default`: ASAuthorizationAppleIDButton.ButtonType](./buttontype/default.md)
  A default button type for the Sign in with Apple authorization process.
- [ASAuthorizationAppleIDButton.ButtonType.signUp](./buttontype/signup.md)
  A button type that allows the user to sign up for Sign in with Apple.
- [ASAuthorizationAppleIDButton.ButtonType.signIn](./buttontype/signin.md)
  A button type that performs authorization using Sign in with Apple.
### Initializers
- [init?(rawValue: Int)](./buttontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Styling the Button
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius, in points, for the rounded corners on the Apple ID sign-in button.
- [ASAuthorizationAppleIDButton.Style](./style.md)
  A style for the authorization button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton/buttontype)*