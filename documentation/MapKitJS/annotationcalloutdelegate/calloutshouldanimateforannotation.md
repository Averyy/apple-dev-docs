# calloutShouldAnimateForAnnotation

**Framework**: MapKit JS  
**Kind**: method

Determines whether the callout animates.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
boolean calloutShouldAnimateForAnnotation(
	mapkit.Annotation annotation
);
```

#### Return Value

This method returns a Boolean value that determines if the callout should be animated.

#### Discussion

This method determines whether an appearance annotation should run. The animation runs if the value is `true`.

## Parameters

- `annotation`: The annotation for the callout.

## See Also

- [calloutAnchorOffsetForAnnotation](annotationcalloutdelegate/calloutanchoroffsetforannotation.md)
  Returns a point determining the callout’s anchor offset.
- [calloutShouldAppearForAnnotation](annotationcalloutdelegate/calloutshouldappearforannotation.md)
  Determines whether the callout appears for an annotation.
- [calloutAppearanceAnimationForAnnotation](annotationcalloutdelegate/calloutappearanceanimationforannotation.md)
  Returns a CSS animation to use when the callout appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate/calloutshouldanimateforannotation)*