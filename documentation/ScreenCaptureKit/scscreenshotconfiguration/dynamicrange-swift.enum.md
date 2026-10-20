# SCScreenshotConfiguration.DynamicRange

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the type of images returned to the client; standard dynamic range, high dynamic range, or both.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
enum DynamicRange
```

```c
enum SCScreenshotDynamicRange : NSInteger;
```

## Topics

### Enumeration Cases
- [SCScreenshotConfiguration.DynamicRange.bothSDRAndHDR](./dynamicrange-swift.enum/bothsdrandhdr.md)
  Returns both standard dynamic range and high dynamic range image versions to the client.
- [SCScreenshotConfiguration.DynamicRange.hdr](./dynamicrange-swift.enum/hdr.md)
  Returns a high dynamic range image to the client.
- [SCScreenshotConfiguration.DynamicRange.sdr](./dynamicrange-swift.enum/sdr.md)
  Returns a standard dynamic range image to the client.
### Initializers
- [init?(rawValue: Int)](./dynamicrange-swift.enum/init%28rawvalue%29.md)
  Creates a dynamic range object from the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/dynamicrange-swift.enum)*