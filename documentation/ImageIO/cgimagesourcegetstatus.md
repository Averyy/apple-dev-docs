# CGImageSourceGetStatus(_:)

**Framework**: Image I/O  
**Kind**: func

Return the status of an image source.

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
func CGImageSourceGetStatus(_ isrc: CGImageSource) -> CGImageSourceStatus
```

#### Return Value

Returns the current status of the image source. See [`CGImageSourceStatus`](cgimagesourcestatus.md) for a list of possible values.

#### Discussion

Status information is particularly informative for incremental image sources, but it may also be useful on image sources that contain non-incremental data.

## Parameters

- `isrc`: The image source that contains the image data.

## See Also

- [func CGImageSourceGetStatusAtIndex(CGImageSource, Int) -> CGImageSourceStatus](cgimagesourcegetstatusatindex(_:_:).md)
  Returns the current status of an image at the specified location in the image source.
- [enum CGImageSourceStatus](cgimagesourcestatus.md)
  The set of status values for images and image sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcegetstatus(_:))*