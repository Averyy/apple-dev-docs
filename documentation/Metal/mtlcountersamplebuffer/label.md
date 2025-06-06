# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the counter sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var label: String { get }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See `Enhancing Frame Capture by Using Labels`.

## See Also

- [var device: any MTLDevice](mtlcountersamplebuffer/device.md)
  The GPU device instance that owns the counter sample buffer.
- [var sampleCount: Int](mtlcountersamplebuffer/samplecount.md)
  The number of samples in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/label)*