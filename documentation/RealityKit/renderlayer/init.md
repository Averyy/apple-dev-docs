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

Use this initializer to define reusable layer constants in an extension. Use descriptive names with namespace prefixes such as `"com.myapp.hero"` or `"com.myapp.background"` to avoid conflicts with other layers.

```swift
extension RenderLayer {
    static let background = RenderLayer("com.myapp.background")
}
```

To create a layer from a runtime string, use [`init(rawValue:)`](renderlayer/init(rawvalue:).md) instead.

> **Note**: The layer name must not be empty.

## Parameters

- `rawValue`: A unique compile-time constant name for this layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/init(_:))*