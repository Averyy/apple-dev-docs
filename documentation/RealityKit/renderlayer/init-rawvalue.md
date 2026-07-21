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

A new render layer, or `nil` if `rawValue` is empty.

#### Discussion

Use this failable initializer when the layer name comes from a runtime string, such as user input or data loaded from a file. To define a layer constant from a string literal, use [`init(_:)`](renderlayer/init(_:).md) instead.

Use descriptive names with namespace prefixes such as `"com.myapp.hero"` or `"com.myapp.background"` to avoid conflicts with other layers.

## Parameters

- `rawValue`: A unique name for this layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/init(rawvalue:))*