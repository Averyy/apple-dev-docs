# notFilterOfSubfilter:

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Type Method

Creates a new filter that excludes the filter you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (PHPickerFilter *) notFilterOfSubfilter:(PHPickerFilter *) subfilter;
```

#### Return Value

A new filter that excludes the filter you specify.

## Parameters

- `subfilter`: The filter to exclude from the new filter.

## See Also

### Creating Filters
- [+ playbackStyleFilter:](./playbackstylefilter_.md)
  Creates a new filter by using the playback style you specify.
- [+ allFilterMatchingSubfilters:](./allfiltermatchingsubfilters_.md)
  Creates a new filter that includes only the filters you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-c.class/notfilterofsubfilter:)*