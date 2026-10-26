# playbackStyle(_:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Type Method

Creates a new filter by using the playback style you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
static func playbackStyle(_ playbackStyle: PHAsset.PlaybackStyle) -> PHPickerFilter
```

#### Return Value

A new filter with the playback style you specify.

## Parameters

- `playbackStyle`: The asset playback style.

## See Also

### Creating Filters
- [static func all(of: [PHPickerFilter]) -> PHPickerFilter](./all%28of%29.md)
  Creates a new filter that includes only the filters you specify.
- [static func not(PHPickerFilter) -> PHPickerFilter](./not%28_%29.md)
  Creates a new filter that excludes the filter you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerfilter-swift.struct/playbackstyle(_:))*