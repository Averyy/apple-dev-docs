# mapkit.Padding

**Framework**: MapKit JS  
**Kind**: init

Creates a padding object and initializes its inset margin properties.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.Padding(
	optional PaddingConstructorOptions options,
	optional number top,
	optional number right,
	optional number bottom,
	optional number left
);
```

#### Discussion

Create [`mapkit.Padding`](mapkit.padding/mapkit.padding.md) by passing in four numbers that represent the inset values from the top, right, bottom, and left edges. Alternatively, use an object literal instance with the keys defined in [`PaddingConstructorOptions`](paddingconstructoroptions.md).

The following examples show two ways to create padding:

```javascript
// example 1: 4 numbers
map.padding = new mapkit.Padding(
    10, // top inset
    10, // right inset
    10, // bottom inset
    10) // left inset

// example 2: object literal conforming to PaddingConstructorOptions
map.padding = new mapkit.Padding({top: 10, right: 10, bottom: 10, left:10})

```

## Parameters

- `top`: An object literal with the keys defined in  , or a list of four numbers that represent inset margin values. The numbers represent the top, right, bottom, and left insets, respectively.

## See Also

- [PaddingConstructorOptions](paddingconstructoroptions.md)
  Initial values of the edge insets for padding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.padding/mapkit.padding)*