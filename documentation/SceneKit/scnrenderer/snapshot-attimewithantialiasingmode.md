# snapshot(atTime:with:antialiasingMode:)

**Framework**: SceneKit  
**Kind**: method

Creates an image by drawing the renderer’s content at the specified system time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func snapshot(atTime time: CFTimeInterval, with size: CGSize, antialiasingMode: SCNAntialiasingMode) -> NSImage
```

#### Return Value

An image object reflecting the contents of the scene.

#### Discussion

When you call this method, SceneKit updates its hierarchy of presentation nodes based on the specified timestamp, and then draws the scene into a new image object of the specified size.

## Parameters

- `time`: The timestamp, in seconds, at which to render the scene.
- `size`: The size, in pixels, of the image to create.
- `antialiasingMode`: The antialiasing mode to use for the image output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/snapshot(attime:with:antialiasingmode:))*