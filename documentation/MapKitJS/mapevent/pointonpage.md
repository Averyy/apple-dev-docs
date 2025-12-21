# pointOnPage

**Framework**: MapKit JS  
**Kind**: property

A DOM point with the coordinate of the event on the page.

**Availability**:
- MapKit JS 5.18+

## Declaration

```swift
readonly pointOnPage?: DOMPoint | undefined;
```

#### Discussion

You can use this property — which is an `(x, y)` coordinate — to derive a latitude and longitude coordinate on the map using [`convertPointOnPageToCoordinate(point)`](map/convertpointonpagetocoordinate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapevent/pointonpage)*