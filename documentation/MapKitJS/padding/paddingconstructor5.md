# new Padding(top, right, bottom, left)

**Framework**: MapKit JS  
**Kind**: init  
**Role**: Constructor

Creates a padding object and initializes it with the provided values.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
constructor(top: number, right: number, bottom: number, left: number);
```

## Discussion

Create [`Padding`](../padding.md) by passing in four numbers that represent the inset values for the top, right, bottom, and left edges.

```javascript
map.padding = new mapkit.Padding(
    10, // top inset
    10, // right inset
    10, // bottom inset
    10 // left inset
);
```

## Parameters

- `top`: The top inset margin.
- `right`: The right inset margin.
- `bottom`: The bottom inset margin.
- `left`: The left inset margin.

## See Also

### Creating padding
- [new Padding()](./paddingconstructor.md)
  Creates a padding object with no inset margins.
- [new Padding(paddings)](./paddingconstructor1.md)
  Creates a padding object and initializes its values with the provided object literal.
- [new Padding(top)](./paddingconstructor2.md)
  Creates a padding object and initializes its top inset margin with the provided value.
- [new Padding(top, right)](./paddingconstructor3.md)
  Creates a padding object and initializes it with the provided top and right side values.
- [new Padding(top, right, bottom)](./paddingconstructor4.md)
  Creates a padding object and initializes it with the provided top, right, and bottom values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/padding/paddingconstructor5)*