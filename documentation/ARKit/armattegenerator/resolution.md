# ARMatteGenerator.Resolution

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

A resolution for a matte texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
enum Resolution
```

```c
enum ARMatteResolution : NSInteger;
```

#### Overview

You generate a matte texture every frame, specifying whether its resolution is the full size or half of the camera image.

## Topics

### Choosing a Resolution Option
- [ARMatteGenerator.Resolution.full](./resolution/full.md)
  An option that specifies the full camera image resolution.
- [ARMatteGenerator.Resolution.half](./resolution/half.md)
  An option that specifies half of the camera image resolution.
### Initializers
- [init?(rawValue: Int)](./resolution/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator/resolution)*