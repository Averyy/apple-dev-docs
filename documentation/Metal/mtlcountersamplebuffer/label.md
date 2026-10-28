# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) NSString * label;
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Inspecting the counter sample buffer’s configuration
- [var device: any MTLDevice](./device.md)
  The GPU device instance that owns the counter sample buffer.
- [var sampleCount: Int](./samplecount.md)
  The number of samples in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/label)*