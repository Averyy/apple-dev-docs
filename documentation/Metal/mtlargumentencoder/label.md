# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [`Naming resources and commands`](https://developer.apple.com/documentation/Xcode/Naming-resources-and-commands).

## See Also

- [var device: any MTLDevice](mtlargumentencoder/device.md)
  The device object that created the argument encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/label)*