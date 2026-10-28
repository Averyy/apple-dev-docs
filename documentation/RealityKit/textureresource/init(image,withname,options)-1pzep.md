# init(image:withName:options:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Synchronously creates a texture resource from an in-memory Core Graphics image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(image cgImage: CGImage, withName resourceName: String? = nil, options: TextureResource.CreateOptions) throws
```

**Other overloads**:

```swift
@MainActor
@preconcurrency convenience init(image cgImage: CGImage, withName resourceName: String? = nil, options: TextureResource.CreateOptions) async throws
```

## Discussion

Loading a [`TextureResource`](../textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](./init%28named,in%29.md) for an example that demonstrates how to safely load content.

This method creates a texture resource from an existing [`CGImage`](../../CoreGraphics/cgimage.md) with specific options.

RealityKit uses the resource name to identify resources, and to match texture resources between networked peers. Specify a unique name for each texture resource you load or generate.

## Parameters

- `cgImage`: The source image.
- `resourceName`: A unique name for syncing the texture resource across the network. The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(image:withname:options:)-1pzep)*