# signal

**Framework**: MapKit JS  
**Kind**: property

A signal object allowing you to cancel the request.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
signal?: AbortSignal;
```

#### Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending points of interest search request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## See Also

- [region](pointsofinterestsearchoptions/region.md)
  The region that bounds the area in which to fetch points of interest.
- [center](pointsofinterestsearchoptions/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](pointsofinterestsearchoptions/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearchoptions/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](serviceconstructoroptions/language.md)
  A language identifier that determines the language for the service results text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearchoptions/signal)*