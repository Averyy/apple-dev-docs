# playbackStyleFilter:

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Type Method

Creates a new filter by using the playback style you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (PHPickerFilter *) playbackStyleFilter:(PHAssetPlaybackStyle) playbackStyle;
```

#### Return Value

A new filter with the playback style you specify.

## Parameters

- `playbackStyle`: The asset playback style.

## See Also

### Creating Filters
- [+ allFilterMatchingSubfilters:](./allfiltermatchingsubfilters_.md)
  Creates a new filter that includes only the filters you specify.
- [+ notFilterOfSubfilter:](./notfilterofsubfilter_.md)
  Creates a new filter that excludes the filter you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-c.class/playbackstylefilter:)*