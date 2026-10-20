# annotationTitles(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Sets the visibility of titles for markers and annotations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func annotationTitles(_ visibility: Visibility) -> some MapContent
```

#### Return Value

Returns [`MapContent`](../mapcontent.md) whose titles have the visibility setting you specified.

## Parameters

- `visibility`: One of the [`Visibility`](../../SwiftUI/visibility.md) settings. The default is [`Visibility.automatic`](../../SwiftUI/visibility/automatic.md) visibility, that results in the title always being visible.

## See Also

### Setting the visibility of the title and subtitle
- [func annotationSubtitles(Visibility) -> some MapContent](./annotationsubtitles%28_%29.md)
  Sets the visibility of subtitles for markers and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent/annotationtitles(_:))*