# PHPickerFilter

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

A type that defines the filter to apply to the photo library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct PHPickerFilter
```

## Topics

### Creating Filters
- [static func playbackStyle(PHAsset.PlaybackStyle) -> PHPickerFilter](./phpickerfilter-swift.struct/playbackstyle%28_%29.md)
  Creates a new filter by using the playback style you specify.
- [static func all(of: [PHPickerFilter]) -> PHPickerFilter](./phpickerfilter-swift.struct/all%28of%29.md)
  Creates a new filter that includes only the filters you specify.
- [static func not(PHPickerFilter) -> PHPickerFilter](./phpickerfilter-swift.struct/not%28_%29.md)
  Creates a new filter that excludes the filter you specify.
### Getting Filter Types
- [static let bursts: PHPickerFilter](./phpickerfilter-swift.struct/bursts.md)
  A filter that represents assets with multiple high-speed photos.
- [static let cinematicVideos: PHPickerFilter](./phpickerfilter-swift.struct/cinematicvideos.md)
  A filter that represents videos with a shallow depth of field and focus transitions.
- [static let depthEffectPhotos: PHPickerFilter](./phpickerfilter-swift.struct/deptheffectphotos.md)
  A filter that represents photos with depth information.
- [static let images: PHPickerFilter](./phpickerfilter-swift.struct/images.md)
  The filter for images.
- [static let livePhotos: PHPickerFilter](./phpickerfilter-swift.struct/livephotos.md)
  The filter for live photos.
- [static let panoramas: PHPickerFilter](./phpickerfilter-swift.struct/panoramas.md)
  A filter that represents panorama photos.
- [static let screenRecordings: PHPickerFilter](./phpickerfilter-swift.struct/screenrecordings.md)
  A filter that represents screen recordings.
- [static let screenshots: PHPickerFilter](./phpickerfilter-swift.struct/screenshots.md)
  A filter that represents screenshots.
- [static let slomoVideos: PHPickerFilter](./phpickerfilter-swift.struct/slomovideos.md)
  A filter that represents slow-motion videos.
- [static let timelapseVideos: PHPickerFilter](./phpickerfilter-swift.struct/timelapsevideos.md)
  A filter that represents time-lapse videos.
- [static let videos: PHPickerFilter](./phpickerfilter-swift.struct/videos.md)
  The filter for videos.
- [static func any(of: [PHPickerFilter]) -> PHPickerFilter](./phpickerfilter-swift.struct/any%28of%29.md)
  Returns a new filter formed by OR-ing the filters in a given array.
### Type Properties
- [static let spatialMedia: PHPickerFilter](./phpickerfilter-swift.struct/spatialmedia.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [class PHPickerViewController](./phpickerviewcontroller.md)
  A view controller that provides the user interface for choosing assets from the photo library.
- [protocol PHPickerViewControllerDelegate](./phpickerviewcontrollerdelegate-5yntc.md)
  A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [struct PHPickerConfiguration](./phpickerconfiguration-swift.struct.md)
  An object that contains information about how to configure a picker view controller.
- [struct PHPickerResult](./phpickerresult-swift.struct.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct)*