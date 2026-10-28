# selectionAccessory

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An accessory that displays place information when a person selects a place.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```
get selectionAccessory(): PlaceSelectionAccessory | null;
set selectionAccessory(value: PlaceSelectionAccessory | null);
```

## Discussion

You need to initialize an annotation with an instance of a [`place`](../annotationconstructoroptions/place.md) so that the accessory displays the correct place.

## See Also

### Managing selection accessories
- [selectionAccessoryOffset](./selectionaccessoryoffset.md)
  An offset that changes the selection accessory’s default anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/selectionaccessory)*