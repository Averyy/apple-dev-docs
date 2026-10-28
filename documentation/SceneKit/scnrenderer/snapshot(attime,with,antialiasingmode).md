# snapshot(atTime:with:antialiasingMode:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Creates an image by drawing the renderer’s content at the specified system time.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func snapshot(atTime time: CFTimeInterval, with size: CGSize, antialiasingMode: SCNAntialiasingMode) -> UIImage
```

*macOS*

```swift
func snapshot(atTime time: CFTimeInterval, with size: CGSize, antialiasingMode: SCNAntialiasingMode) -> NSImage
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (UIImage *) snapshotAtTime:(CFTimeInterval) time withSize:(CGSize) size antialiasingMode:(SCNAntialiasingMode) antialiasingMode;
```

*macOS*

```objc
- (NSImage *) snapshotAtTime:(CFTimeInterval) time withSize:(CGSize) size antialiasingMode:(SCNAntialiasingMode) antialiasingMode;
```

## Return Value

An image object reflecting the contents of the scene.

## Discussion

When you call this method, SceneKit updates its hierarchy of presentation nodes based on the specified timestamp, and then draws the scene into a new image object of the specified size.

## Parameters

- `time`: The timestamp, in seconds, at which to render the scene.
- `size`: The size, in pixels, of the image to create.
- `antialiasingMode`: The antialiasing mode to use for the image output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/snapshot(attime:with:antialiasingmode:))*