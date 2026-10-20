# MTLDeviceError.Code

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Enumeration of kinds of errors that methods on MTLDevice can produce.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
enum Code
```

```c
enum MTLDeviceError : NSInteger;
```

## Topics

### Enumeration Cases
- [MTLDeviceError.Code.none](./code/none.md)
  Indicates the absence of any problems.
- [MTLDeviceError.Code.notSupported](./code/notsupported.md)
  Indicates the requested feature is not supported by the current device.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldeviceerror-swift.struct/code)*