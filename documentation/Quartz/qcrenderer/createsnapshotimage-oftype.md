# createSnapshotImage(ofType:)

**Framework**: Quartz  
**Kind**: method

Returns the current image in the OpenGL context associated with the renderer, as an image object of the provided image type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func createSnapshotImage(ofType type: String!) -> Any!
```

#### Return Value

The snapshot image in the provided image type. You are responsible for releasing this object when you no longer need it.

## Parameters

- `type`: A string that specifies any of the following image types:  ,  ,  ,  ,  ,  .

## See Also

- [func snapshotImage() -> NSImage!](qcrenderer/snapshotimage.md)
  Returns an `NSImage` object of the current image in the OpenGL context associated with the renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/createsnapshotimage(oftype:))*