# calloutAppearanceAnimationForAnnotation(annotation)

**Framework**: MapKit JS  
**Kind**: method

Returns a CSS animation to use when the callout appears.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
calloutAppearanceAnimationForAnnotation?(annotation: Annotation): string;
```

#### Return Value

This method returns a string that describes the CSS animation to use for the callout appearance, just like the [`appearanceAnimation`](annotation/appearanceanimation.md) property of [`Annotation`](annotation.md).

#### Discussion

To animate a callout, MapKit JS calls this method on the annotation’s callout delegate with the annotation as a parameter. A standard callout (with or without custom content) uses a default animation if the callout doesn’t provide the appearance animation.

A callout that uses a custom element can animate only if it provides the appearance animation. The default animation doesn’t apply to callouts with custom elements.

## Parameters

- `annotation`: The annotation for the callout.

## See Also

- [calloutAnchorOffsetForAnnotation(annotation, size)](annotationcalloutdelegate/calloutanchoroffsetforannotation.md)
  Returns a point determining the callout’s anchor offset.
- [calloutShouldAppearForAnnotation(annotation)](annotationcalloutdelegate/calloutshouldappearforannotation.md)
  Determines whether the callout appears for an annotation.
- [calloutShouldAnimateForAnnotation(annotation)](annotationcalloutdelegate/calloutshouldanimateforannotation.md)
  Determines whether the callout animates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate/calloutappearanceanimationforannotation)*