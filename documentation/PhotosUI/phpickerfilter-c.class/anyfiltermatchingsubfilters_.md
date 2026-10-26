# anyFilterMatchingSubfilters:

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Type Method

Creates a new filter by combining the filters in the array.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (PHPickerFilter *) anyFilterMatchingSubfilters:(NSArray<PHPickerFilter *> *) subfilters;
```

#### Return Value

A new picker filter.

## Parameters

- `subfilters`: The list of filters to combine into a new filter.

## See Also

### Comparing Filters
- [imagesFilter](./imagesfilter.md)
  A filter that represents images, and includes Live Photos.
- [livePhotosFilter](./livephotosfilter.md)
  A filter that represents Live Photos.
- [videosFilter](./videosfilter.md)
  A filter that represents video assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-c.class/anyfiltermatchingsubfilters:)*