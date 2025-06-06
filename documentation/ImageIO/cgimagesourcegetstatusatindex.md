# CGImageSourceGetStatusAtIndex(_:_:)

**Framework**: Image I/O  
**Kind**: func

Returns the current status of an image at the specified location in the image source.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageSourceGetStatusAtIndex(_ isrc: CGImageSource, _ index: Int) -> CGImageSourceStatus
```

#### Return Value

Returns the current status of the image. See [`CGImageSourceStatus`](cgimagesourcestatus.md) for a list of possible values.

#### Discussion

Status information is particularly informative for incremental image sources, but you may also use it on image sources that contain non-incremental data.

## Parameters

- `isrc`: The image source that contains the image data.
- `index`: The zero-based index into the images of the image source. If the index is invalid, this method returns  .

## See Also

- [func CGImageSourceGetStatus(CGImageSource) -> CGImageSourceStatus](cgimagesourcegetstatus(_:).md)
  Return the status of an image source.
- [enum CGImageSourceStatus](cgimagesourcestatus.md)
  The set of status values for images and image sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcegetstatusatindex(_:_:))*