# calloutEnabled

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether the map shows an annotation’s callout.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get calloutEnabled(): boolean;
set calloutEnabled(value: boolean);
```

#### Discussion

If the [`title`](annotation/title.md) is empty, the framework can’t show the standard callout even if this property is `true`.

## See Also

- [callout](annotation/callout.md)
  A delegate that enables you to customize the annotation’s callout.
- [calloutOffset](annotation/calloutoffset.md)
  An offset that changes the annotation callout’s default placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/calloutenabled)*