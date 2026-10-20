# setSelected(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Sets the selection state of the annotation view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func setSelected(_ selected: Bool, animated: Bool)
```

```objc
- (void) setSelected:(BOOL) selected animated:(BOOL) animated;
```

#### Discussion

Dont call this method directly. An [`MKMapView`](../mkmapview.md) object calls this method in response to user interactions with the annotation.

## Parameters

- `selected`: Contains the value [`true`](../../Swift/true.md) if the view displays in a selected state.
- `animated`: Set to [`true`](../../Swift/true.md) if the map view animates the change in selection state.

## See Also

### Related Documentation
- [func selectAnnotation(any MKAnnotation, animated: Bool)](../mkmapview/selectannotation%28_,animated%29.md)
  Selects the specified annotation and displays a callout view for it.
### Managing the selection state
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the annotation view is in a selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/setselected(_:animated:))*