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

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [`Naming resources and commands`](https://developer.apple.com/documentation/Xcode/Naming-resources-and-commands).

## See Also

- [var device: any MTLDevice](mtldynamiclibrary/device.md)
  The Metal device object that created the dynamic library.
- [var installName: String](mtldynamiclibrary/installname.md)
  A file path for this dynamic library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldynamiclibrary/label)*