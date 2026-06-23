# setTexture(_:port:)

**Framework**: RealityKit  
**Kind**: method

Binds a Metal texture to a parameter identified by its port address.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func setTexture(_ texture: (any MTLTexture)?, port: ComputeNodeGraph.Port.Address) -> Bool
```

#### Return Value

`true` if the port was found and the texture was set; `false` otherwise.

## Parameters

- `texture`: The `MTLTexture` to bind, or `nil` to unbind the current texture.
- `port`: The port address identifying the texture parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/settexture(_:port:))*