# calloutRightAccessoryForAnnotation(annotation)

**Framework**: MapKit JS  
**Kind**: method

Returns an element to use as a custom accessory on the right side of the callout content area.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
calloutRightAccessoryForAnnotation?(annotation: Annotation): HTMLElement;
```

#### Return Value

This method returns a DOM element to display as the right accessory.

#### Discussion

You can use this method to provide a custom accessory to the right side of the callout content area. It works similarly to [`calloutLeftAccessoryForAnnotation(annotation)`](annotationcalloutdelegate/calloutleftaccessoryforannotation.md).

## Parameters

- `annotation`: The annotation for the callout.

## See Also

- [calloutContentForAnnotation(annotation)](annotationcalloutdelegate/calloutcontentforannotation.md)
  Returns custom content for the callout bubble.
- [calloutElementForAnnotation(annotation)](annotationcalloutdelegate/calloutelementforannotation.md)
  Returns an element representing a custom callout.
- [calloutLeftAccessoryForAnnotation(annotation)](annotationcalloutdelegate/calloutleftaccessoryforannotation.md)
  Returns an element to use as a custom accessory on the left side of the callout content area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate/calloutrightaccessoryforannotation)*