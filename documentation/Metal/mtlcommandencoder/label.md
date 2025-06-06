# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that labels the command encoder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See `Enhancing Frame Capture by Using Labels`.

## See Also

- [var device: any MTLDevice](mtlcommandencoder/device.md)
  The Metal device from which the command encoder was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/label)*