# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the sampler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [`Naming resources and commands`](https://developer.apple.com/documentation/Xcode/Naming-resources-and-commands).

## See Also

- [var device: any MTLDevice](mtlsamplerstate/device.md)
  The device object that created the sampler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerstate/label)*