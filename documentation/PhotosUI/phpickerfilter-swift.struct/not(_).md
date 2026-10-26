# not(_:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Type Method

Creates a new filter that excludes the filter you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
static func not(_ filter: PHPickerFilter) -> PHPickerFilter
```

#### Return Value

A new filter that excludes the filter you specify.

## Parameters

- `filter`: The filter to exclude from the new filter.

## See Also

### Creating Filters
- [static func playbackStyle(PHAsset.PlaybackStyle) -> PHPickerFilter](./playbackstyle%28_%29.md)
  Creates a new filter by using the playback style you specify.
- [static func all(of: [PHPickerFilter]) -> PHPickerFilter](./all%28of%29.md)
  Creates a new filter that includes only the filters you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct/not(_:))*