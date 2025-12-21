# animates

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether the framework animates the annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get animates(): boolean;
set animates(value: boolean);
```

#### Discussion

When this property is `true`, MapKit JS animates the appearance of the annotation on the map. You’re responsible for implementing an animation using the [`appearanceAnimation`](annotation/appearanceanimation.md) property.

The annotation doesn’t animate when:

- You don’t provide an animation in [`appearanceAnimation`](annotation/appearanceanimation.md).
- The [`animates`](annotation/animates.md) property is `false.`

## See Also

- [draggable](annotation/draggable.md)
  A Boolean value that determines whether the user can drag the annotation.
- [selected](annotation/selected.md)
  A Boolean value that indicates whether the map shows the annotation in a selected state.
- [enabled](annotation/enabled.md)
  A Boolean value that determines whether the annotation responds to user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/animates)*