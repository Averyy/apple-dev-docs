# setSelected(_:animated:)

**Framework**: MapKit  
**Kind**: method

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
@MainActor
func setSelected(_ selected: Bool, animated: Bool)
```

#### Discussion

Dont call this method directly. An [`MKMapView`](mkmapview.md) object calls this method in response to user interactions with the annotation.

## Parameters

- `selected`: Contains the value   if the view displays in a selected state.
- `animated`: Set to   if the map view animates the change in selection state.

## See Also

- [func selectAnnotation(any MKAnnotation, animated: Bool)](mkmapview/selectannotation(_:animated:).md)
  Selects the specified annotation and displays a callout view for it.
- [var isSelected: Bool](mkannotationview/isselected.md)
  A Boolean value that indicates whether the annotation view is in a selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/setselected(_:animated:))*