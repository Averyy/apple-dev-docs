# name

**Framework**: RealityKit  
**Kind**: property

The name of the surface shader function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
var name: String
```

#### Discussion

This is the name of the Metal function the custom material uses as its surface shader. The name needs to match the name of a Metal function in your Xcode project and can’t include parameters or parentheses.

## See Also

- [var library: any MTLLibrary](custommaterial/surfaceshader/library.md)
  The Metal library that contains this surface shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/surfaceshader/name)*