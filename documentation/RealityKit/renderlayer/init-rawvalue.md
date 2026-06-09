# init(rawValue:)

**Framework**: RealityKit  
**Kind**: init

Creates a custom render layer with the specified runtime name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init?(rawValue: String)
```

#### Return Value

A new `RenderLayer` instance, or `nil` if the name is invalid.

#### Discussion

This failable initializer allows creating layers from runtime string values, such as user input or data loaded from files. Returns `nil` if the layer name is invalid (empty).

Use descriptive names with namespace prefixes to avoid conflicts, such as `"com.myapp.hero-lighting"` or `"com.myapp.background"`.

## Parameters

- `rawValue`: A unique name for this layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/init(rawvalue:))*