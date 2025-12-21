# calloutElementForAnnotation(annotation)

**Framework**: MapKit JS  
**Kind**: method

Returns an element representing a custom callout.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
calloutElementForAnnotation?(annotation: Annotation): HTMLElement;
```

#### Return Value

This method returns a DOM element to use as the callout element in place of the standard callout bubble. This callout element populates with the information to display, including the information from the annotation.

#### Discussion

If you don’t prevent the callout from appearing, MapKit JS calls this method on the annotation’s callout delegate (if the delegate is an object and its [`calloutElementForAnnotation(annotation)`](annotationcalloutdelegate/calloutelementforannotation.md) property is a function) with the annotation as a parameter.

## Parameters

- `annotation`: The annotation for the callout.

## See Also

- [calloutContentForAnnotation(annotation)](annotationcalloutdelegate/calloutcontentforannotation.md)
  Returns custom content for the callout bubble.
- [calloutLeftAccessoryForAnnotation(annotation)](annotationcalloutdelegate/calloutleftaccessoryforannotation.md)
  Returns an element to use as a custom accessory on the left side of the callout content area.
- [calloutRightAccessoryForAnnotation(annotation)](annotationcalloutdelegate/calloutrightaccessoryforannotation.md)
  Returns an element to use as a custom accessory on the right side of the callout content area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate/calloutelementforannotation)*