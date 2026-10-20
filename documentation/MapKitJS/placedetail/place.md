# place

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The place that the place detail displays.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```
get place(): Place | null;
set place(value: Place | null);
```

#### Discussion

if this property is `null`, the place detail renders in a collapsed state and doesn’t show any information.

## See Also

### Working with place detail settings
- [colorScheme](./colorscheme.md)
  The color scheme when displaying a place detail.
- [displaysMap](./displaysmap.md)
  A Boolean value that indicates whether to display the map in the place detail.
- [element](./element.md)
  The place detail’s DOM element.
- [ColorSchemes](./colorschemes.md)
  A static property that allows you to access the Look Around color scheme enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placedetail/place)*