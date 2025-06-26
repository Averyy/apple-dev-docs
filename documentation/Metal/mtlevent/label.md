# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the event.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [`Naming resources and commands`](https://developer.apple.com/documentation/Xcode/Naming-resources-and-commands).

## See Also

- [var device: (any MTLDevice)?](mtlevent/device.md)
  The device object that created the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlevent/label)*