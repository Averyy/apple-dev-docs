# any(of:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Type Method

Returns a new filter formed by OR-ing the filters in a given array.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
static func any(of subfilters: [PHPickerFilter]) -> PHPickerFilter
```

## See Also

### Getting Filter Types
- [static let bursts: PHPickerFilter](./bursts.md)
  A filter that represents assets with multiple high-speed photos.
- [static let cinematicVideos: PHPickerFilter](./cinematicvideos.md)
  A filter that represents videos with a shallow depth of field and focus transitions.
- [static let depthEffectPhotos: PHPickerFilter](./deptheffectphotos.md)
  A filter that represents photos with depth information.
- [static let images: PHPickerFilter](./images.md)
  The filter for images.
- [static let livePhotos: PHPickerFilter](./livephotos.md)
  The filter for live photos.
- [static let panoramas: PHPickerFilter](./panoramas.md)
  A filter that represents panorama photos.
- [static let screenRecordings: PHPickerFilter](./screenrecordings.md)
  A filter that represents screen recordings.
- [static let screenshots: PHPickerFilter](./screenshots.md)
  A filter that represents screenshots.
- [static let slomoVideos: PHPickerFilter](./slomovideos.md)
  A filter that represents slow-motion videos.
- [static let timelapseVideos: PHPickerFilter](./timelapsevideos.md)
  A filter that represents time-lapse videos.
- [static let videos: PHPickerFilter](./videos.md)
  The filter for videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct/any(of:))*