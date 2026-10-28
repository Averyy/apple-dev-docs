# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The GPU device instance that owns the counter sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (readonly) id<MTLDevice> device;
```

## Discussion

You can store a GPU device’s counter set data only with a counter sample buffer that you create from the same device.

## See Also

### Inspecting the counter sample buffer’s configuration
- [var label: String](./label.md)
  A string that identifies the counter sample buffer.
- [var sampleCount: Int](./samplecount.md)
  The number of samples in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/device)*