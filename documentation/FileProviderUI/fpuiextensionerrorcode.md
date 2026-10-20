# FPUIExtensionErrorCode

**Framework**: File Provider UI  
**Kind**: enum  
**Role**: Enumeration

The error codes for errors raised by the File Provider UI extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum FPUIExtensionErrorCode
```

```c
enum FPUIExtensionErrorCode : NSUInteger;
```

## Topics

### Error Codes
- [FPUIExtensionErrorCode.failed](./fpuiextensionerrorcode/failed.md)
  An error indicating that the action has failed.
- [FPUIExtensionErrorCode.userCancelled](./fpuiextensionerrorcode/usercancelled.md)
  An error indicating that the action was canceled by the user.
### Initializers
- [init?(rawValue: UInt)](./fpuiextensionerrorcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [let FPUIErrorDomain: String](./fpuierrordomain.md)
  The error domain for errors raised by the File Provider UI extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiextensionerrorcode)*