# calloutShouldAppearForAnnotation(annotation)

**Framework**: MapKit JS  
**Kind**: method

Determines whether the callout appears for an annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
calloutShouldAppearForAnnotation?(annotation: Annotation): boolean;
```

#### Return Value

The method returns a Boolean value, where a value of `false` prevents the callout from appearing.

#### Discussion

When the user selects an annotation, MapKit JS calls this method on the annotation’s callout delegate (if the delegate is an object and its [`calloutShouldAppearForAnnotation(annotation)`](annotationcalloutdelegate/calloutshouldappearforannotation.md) property is a function) with the annotation as a parameter.

## Parameters

- `annotation`: The annotation for the callout.

## See Also

- [calloutAnchorOffsetForAnnotation(annotation, size)](annotationcalloutdelegate/calloutanchoroffsetforannotation.md)
  Returns a point determining the callout’s anchor offset.
- [calloutShouldAnimateForAnnotation(annotation)](annotationcalloutdelegate/calloutshouldanimateforannotation.md)
  Determines whether the callout animates.
- [calloutAppearanceAnimationForAnnotation(annotation)](annotationcalloutdelegate/calloutappearanceanimationforannotation.md)
  Returns a CSS animation to use when the callout appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate/calloutshouldappearforannotation)*