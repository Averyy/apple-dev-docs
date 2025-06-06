# annotationTitles(_:)

**Framework**: MapKit  
**Kind**: method

Sets the visibility of titles for markers and annotations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func annotationTitles(_ visibility: Visibility) -> some MapContent
```

#### Return Value

Returns [`MapContent`](mapcontent.md) whose titles have the visibility setting you specified.

## Parameters

- `visibility`: One of the   settings. The default is   visibility, that results in the title always being visible.

## See Also

- [func annotationSubtitles(Visibility) -> some MapContent](mapcontent/annotationsubtitles(_:).md)
  Sets the visibility of subtitles for markers and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/annotationtitles(_:))*