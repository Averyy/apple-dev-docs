# new Padding(paddings)

**Framework**: MapKit JS  
**Kind**: init  
**Role**: Constructor

Creates a padding object and initializes its values with the provided object literal.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
constructor(paddings: PaddingData);
```

## Discussion

Use an object literal instance with the keys defined in [`PaddingData`](../paddingdata.md).

```javascript
    // An object literal that conforms to `PaddingData`.
    map.padding = new mapkit.Padding({top: 10, right: 10, bottom: 10, left:10});
```

## Parameters

- `padding`: An object literal with the keys defined in [`PaddingData`](../paddingdata.md).

## See Also

### Creating padding
- [new Padding()](./paddingconstructor.md)
  Creates a padding object with no inset margins.
- [new Padding(top)](./paddingconstructor2.md)
  Creates a padding object and initializes its top inset margin with the provided value.
- [new Padding(top, right)](./paddingconstructor3.md)
  Creates a padding object and initializes it with the provided top and right side values.
- [new Padding(top, right, bottom)](./paddingconstructor4.md)
  Creates a padding object and initializes it with the provided top, right, and bottom values.
- [new Padding(top, right, bottom, left)](./paddingconstructor5.md)
  Creates a padding object and initializes it with the provided values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/padding/paddingconstructor1)*