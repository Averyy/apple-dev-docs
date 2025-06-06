# createSnapshotImage(ofType:)

**Framework**: Quartz  
**Kind**: method

Returns the current image in the view as an image object of the provided image type.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func createSnapshotImage(ofType type: String!) -> Any!
```

#### Return Value

The snapshot image  in the provided image type. You are responsible for releasing this object when you no longer need it.

## Parameters

- `type`: A string that specifies any of the following image types:  ,  ,  ,  ,  ,  .

## See Also

- [func snapshotImage() -> NSImage!](qcview/snapshotimage.md)
  Returns an `NSImage` object of the current image in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/createsnapshotimage(oftype:))*