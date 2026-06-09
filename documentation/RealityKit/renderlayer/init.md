# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a custom render layer with the specified compile-time constant name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ rawValue: StaticString)
```

#### Discussion

This initializer accepts only compile-time string constants. A precondition checks the validity of the layer name. Use this for defining layer constants in extensions of RenderLayer.

It is recommended to use descriptive names with namespace prefixes to avoid conflicts, such as `"com.myapp.hero-lighting"` or `"com.myapp.background"`.

This can look like layer constants as extensions:

```swift
extension RenderLayer {
    static let background = RenderLayer("com.myapp.background")
}
```

> **Note**: The layer name must not be empty.

## Parameters

- `rawValue`: A unique compile-time constant name for this layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/init(_:))*