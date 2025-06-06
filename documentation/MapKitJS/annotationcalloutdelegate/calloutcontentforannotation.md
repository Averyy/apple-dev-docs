# calloutContentForAnnotation

**Framework**: MapKit JS  
**Kind**: method

Returns custom content for the callout bubble.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
Element calloutContentForAnnotation(
	mapkit.Annotation annotation
);
```

#### Return Value

The method returns a DOM element, MapKit JS adds as a subelement of the callout bubble.

#### Discussion

You can use this method to provide custom content inside the callout bubble without replacing the whole element, as in [`calloutElementForAnnotation`](annotationcalloutdelegate/calloutelementforannotation.md).

When MapKit JS creates a callout for a selected annotation and the annotation’s callout delegate has no [`calloutElementForAnnotation`](annotationcalloutdelegate/calloutelementforannotation.md) method, the framework calls [`calloutContentForAnnotation`](annotationcalloutdelegate/calloutcontentforannotation.md) method instead — if it’s defined — on the delegate with the annotation as a parameter.

## Parameters

- `annotation`: The annotation for the callout.

## See Also

- [calloutElementForAnnotation](annotationcalloutdelegate/calloutelementforannotation.md)
  Returns an element representing a custom callout.
- [calloutLeftAccessoryForAnnotation](annotationcalloutdelegate/calloutleftaccessoryforannotation.md)
  Returns an element to use as a custom accessory on the left side of the callout content area.
- [calloutRightAccessoryForAnnotation](annotationcalloutdelegate/calloutrightaccessoryforannotation.md)
  Returns an element to use as a custom accessory on the right side of the callout content area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate/calloutcontentforannotation)*