# CXHandle.HandleType

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

The possible types of handles.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum HandleType
```

```c
enum CXHandleType : NSInteger;
```

## Topics

### Constants
- [CXHandle.HandleType.generic](./handletype/generic.md)
  An unspecified type of handle.
- [CXHandle.HandleType.phoneNumber](./handletype/phonenumber.md)
  A phone number.
- [CXHandle.HandleType.emailAddress](./handletype/emailaddress.md)
  An email address.
### Initializers
- [init?(rawValue: Int)](./handletype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxhandle/handletype)*