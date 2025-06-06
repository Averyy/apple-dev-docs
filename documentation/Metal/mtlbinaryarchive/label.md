# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See `Enhancing Frame Capture by Using Labels`.

## See Also

- [var device: any MTLDevice](mtlbinaryarchive/device.md)
  The Metal device object that created the binary archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive/label)*