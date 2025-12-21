# map

**Framework**: MapKit JS  
**Kind**: property

The map that the framework adds the annotation to.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get map(): Map | null;
set map(_: Map | null);
```

#### Discussion

This property is `null` before MapKit JS adds the annotation to a [`Map`](map.md), and after MapKit JS removes the annotation from a `mapkit.Map`.

## See Also

- [element](annotation/element.md)
  The annotation’s element in the DOM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/map)*