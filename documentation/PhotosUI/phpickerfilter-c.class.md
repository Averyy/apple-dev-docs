# PHPickerFilter

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

A type that defines the filter to apply to the photo library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
@interface PHPickerFilter : NSObject
```

## Topics

### Creating Filters
- [+ playbackStyleFilter:](./phpickerfilter-c.class/playbackstylefilter_.md)
  Creates a new filter by using the playback style you specify.
- [+ allFilterMatchingSubfilters:](./phpickerfilter-c.class/allfiltermatchingsubfilters_.md)
  Creates a new filter that includes only the filters you specify.
- [+ notFilterOfSubfilter:](./phpickerfilter-c.class/notfilterofsubfilter_.md)
  Creates a new filter that excludes the filter you specify.
### Getting Filter Constants
- [burstsFilter](./phpickerfilter-c.class/burstsfilter.md)
  A filter that represents assets with multiple high-speed photos.
- [cinematicVideosFilter](./phpickerfilter-c.class/cinematicvideosfilter.md)
  A filter that represents videos with a shallow depth of field and focus transitions.
- [depthEffectPhotosFilter](./phpickerfilter-c.class/deptheffectphotosfilter.md)
  A filter that represents photos with depth information.
- [panoramasFilter](./phpickerfilter-c.class/panoramasfilter.md)
  A filter that represents panorama photos.
- [screenRecordingsFilter](./phpickerfilter-c.class/screenrecordingsfilter.md)
  A filter that represents screen recordings.
- [screenshotsFilter](./phpickerfilter-c.class/screenshotsfilter.md)
  A filter that represents screenshots.
- [slomoVideosFilter](./phpickerfilter-c.class/slomovideosfilter.md)
  A filter that represents slow-motion videos.
- [timelapseVideosFilter](./phpickerfilter-c.class/timelapsevideosfilter.md)
  A filter that represents time-lapse videos.
### Comparing Filters
- [imagesFilter](./phpickerfilter-c.class/imagesfilter.md)
  A filter that represents images, and includes Live Photos.
- [livePhotosFilter](./phpickerfilter-c.class/livephotosfilter.md)
  A filter that represents Live Photos.
- [videosFilter](./phpickerfilter-c.class/videosfilter.md)
  A filter that represents video assets.
- [+ anyFilterMatchingSubfilters:](./phpickerfilter-c.class/anyfiltermatchingsubfilters_.md)
  Creates a new filter by combining the filters in the array.
### Type Properties
- [spatialMediaFilter](./phpickerfilter-c.class/spatialmediafilter.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [class PHPickerViewController](./phpickerviewcontroller.md)
  A view controller that provides the user interface for choosing assets from the photo library.
- [PHPickerConfiguration](./phpickerconfiguration-c.class.md)
  An object that contains information about how to configure a picker view controller.
- [PHPickerResult](./phpickerresult-c.class.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-c.class)*