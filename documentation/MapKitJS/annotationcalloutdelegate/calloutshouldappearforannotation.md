# calloutShouldAppearForAnnotation(annotation)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Determines whether the callout appears for an annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
calloutShouldAppearForAnnotation?(annotation: Annotation): boolean;
```

#### Return Value

The method returns a Boolean value, where a value of `false` prevents the callout from appearing.

#### Discussion

When the user selects an annotation, MapKit JS calls this method on the annotation’s callout delegate (if the delegate is an object and its [`calloutShouldAppearForAnnotation()`](./calloutshouldappearforannotation.md) property is a function) with the annotation as a parameter.

## Parameters

- `annotation`: The annotation for the callout.

## See Also

### Customizing callout appearance
- [calloutAnchorOffsetForAnnotation(annotation, size)](./calloutanchoroffsetforannotation.md)
  Returns a point determining the callout’s anchor offset.
- [calloutShouldAnimateForAnnotation(annotation)](./calloutshouldanimateforannotation.md)
  Determines whether the callout animates.
- [calloutAppearanceAnimationForAnnotation(annotation)](./calloutappearanceanimationforannotation.md)
  Returns a CSS animation to use when the callout appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate/calloutshouldappearforannotation)*