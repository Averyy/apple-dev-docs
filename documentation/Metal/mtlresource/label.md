# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the resource.

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

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [`Naming resources and commands`](https://developer.apple.com/documentation/Xcode/Naming-resources-and-commands).

## See Also

- [var device: any MTLDevice](mtlresource/device.md)
  The device object that created the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/label)*