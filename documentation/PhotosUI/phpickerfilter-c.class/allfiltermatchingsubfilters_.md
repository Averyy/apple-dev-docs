# allFilterMatchingSubfilters:

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Type Method

Creates a new filter that includes only the filters you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (PHPickerFilter *) allFilterMatchingSubfilters:(NSArray<PHPickerFilter *> *) subfilters;
```

## Return Value

A new filter that contains the list of filters you specify.

## Parameters

- `subfilters`: The array of filters to include.

## See Also

### Creating Filters
- [+ playbackStyleFilter:](./playbackstylefilter_.md)
  Creates a new filter by using the playback style you specify.
- [+ notFilterOfSubfilter:](./notfilterofsubfilter_.md)
  Creates a new filter that excludes the filter you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-c.class/allfiltermatchingsubfilters:)*