# sampleCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The number of samples in the buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sampleCount: Int { get }
```

```objc
@property (readonly) NSUInteger sampleCount;
```

## See Also

### Inspecting the counter sample buffer’s configuration
- [var label: String](./label.md)
  A string that identifies the counter sample buffer.
- [var device: any MTLDevice](./device.md)
  The GPU device instance that owns the counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/samplecount)*