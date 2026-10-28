# animates

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the framework animates the annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get animates(): boolean;
set animates(value: boolean);
```

## Discussion

When this property is `true`, MapKit JS animates the appearance of the annotation on the map. You’re responsible for implementing an animation using the [`appearanceAnimation`](./appearanceanimation.md) property.

The annotation doesn’t animate when:

- You don’t provide an animation in [`appearanceAnimation`](./appearanceanimation.md).
- The [`animates`](./animates.md) property is `false.`

## See Also

### Getting and setting interaction behavior
- [draggable](./draggable.md)
  A Boolean value that determines whether the user can drag the annotation.
- [selected](./selected.md)
  A Boolean value that indicates whether the map shows the annotation in a selected state.
- [enabled](./enabled.md)
  A Boolean value that determines whether the annotation responds to user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/animates)*