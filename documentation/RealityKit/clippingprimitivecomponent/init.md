# init()

**Framework**: RealityKit  
**Kind**: init

Creates a Clipping Primitive Component with default settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init()
```

#### Discussion

The default configuration creates a clipping volume with:

- A zero-size bounding box at the origin
- Linear falloff with no feathering on any edges
- Clipping applied to self but not children


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingprimitivecomponent/init())*