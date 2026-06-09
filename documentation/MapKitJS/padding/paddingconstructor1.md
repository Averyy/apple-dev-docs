# new Padding(paddings)

**Framework**: MapKit JS  
**Kind**: init

Creates a padding object and initializes its values with the provided object literal.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(paddings: PaddingData);
```

#### Discussion

Use an object literal instance with the keys defined in [`PaddingData`](paddingdata.md).

```javascript
    // An object literal that conforms to `PaddingData`.
    map.padding = new mapkit.Padding({top: 10, right: 10, bottom: 10, left:10});
```

## Parameters

- `padding`: An object literal with the keys defined in [`PaddingData`](paddingdata.md).

## See Also

- [new Padding()](padding/paddingconstructor.md)
  Creates a padding object with no inset margins.
- [new Padding(top)](padding/paddingconstructor2.md)
  Creates a padding object and initializes its top inset margin with the provided value.
- [new Padding(top, right)](padding/paddingconstructor3.md)
  Creates a padding object and initializes it with the provided top and right side values.
- [new Padding(top, right, bottom)](padding/paddingconstructor4.md)
  Creates a padding object and initializes it with the provided top, right, and bottom values.
- [new Padding(top, right, bottom, left)](padding/paddingconstructor5.md)
  Creates a padding object and initializes it with the provided values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/padding/paddingconstructor1)*