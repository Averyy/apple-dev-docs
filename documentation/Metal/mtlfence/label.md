# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the fence.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See `Enhancing Frame Capture by Using Labels`.

## See Also

- [var device: any MTLDevice](mtlfence/device.md)
  The device object that created the fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfence/label)*