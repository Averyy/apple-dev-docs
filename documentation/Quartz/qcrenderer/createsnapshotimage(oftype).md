# createSnapshotImage(ofType:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the current image in the OpenGL context associated with the renderer, as an image object of the provided image type.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func createSnapshotImage(ofType type: String!) -> Any!
```

```objc
- (id) createSnapshotImageOfType:(NSString *) type;
```

#### Return Value

The snapshot image in the provided image type. You are responsible for releasing this object when you no longer need it.

## Parameters

- `type`: A string that specifies any of the following image types: [`NSBitmapImageRep`](../../AppKit/nsbitmapimagerep.md), [`NSImage`](../../AppKit/nsimage.md), [`CIImage`](../../CoreImage/ciimage.md), `CGImage`, `CVOpenGLBuffer`, `CVPixelBuffer`.

## See Also

### Taking Snapshot Images
- [func snapshotImage() -> NSImage!](./snapshotimage%28%29.md)
  Returns an `NSImage` object of the current image in the OpenGL context associated with the renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/createsnapshotimage(oftype:))*