# size

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The desired dimensions of the annotation, in CSS pixels.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get size(): Size | null;
set size(value: Size);
```

## Discussion

If supplied, indicates the desired size of the annotation in CSS pixels. The value must be an object with `width` and `height` number properties:

```javascript
{
    size: { width: 32, height: 39 }
}
```

## See Also

### Getting and setting annotation appearance
- [coordinate](./coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](./anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](./appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](./displaypriority-data.property.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [padding](./padding.md)
  Spacing to add around the annotation when showing items.
- [visible](./visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/size)*