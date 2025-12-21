# new Padding(paddings)

**Framework**: MapKit JS  
**Kind**: init

Creates a padding object and initializes its values with the provided object literal.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(paddings: PaddingConstructorOptions);
```

#### Discussion

Use an object literal instance with the keys defined in [`PaddingConstructorOptions`](paddingconstructoroptions.md).

```javascript
    // An object literal that conforms to `PaddingConstructorOptions`.
    map.padding = new mapkit.Padding({top: 10, right: 10, bottom: 10, left:10});

@Comment {
    This document is generated from symbols produced
    from the MapKit JS source code.
    Feel free to remove this comment when the content is populated.
}
```

## Parameters

- `padding`: An object literal with the keys defined in  .

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
- [interface PaddingConstructorOptions](paddingconstructoroptions.md)
  Initial values of the edge insets for padding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/padding/paddingconstructor1)*