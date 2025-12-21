# Time (float)

**Framework**: ShaderGraph  
**Kind**: subscript

The current time in seconds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Discussion

The `Time` node outputs a float that represents the current time in seconds. When applied or connected to other nodes, this value changes constantly, allowing for dynamic materials. Below is an example of a simple node graph that causes an image texture to scroll in real time:

![None](https://docs-assets.developer.apple.com/published/cff64c2ca64dd8e94442e51f2b648d9f/TimeGraph.png)

Adding Time to the incoming texture coordinates horizontal component causes the texture to “scroll” along the horizontal plane. Below, the resulting texture applies to a cube:

## See Also

- [Up Direction](application/up-direction.md)
  The direction of the up vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/application/time-(float))*