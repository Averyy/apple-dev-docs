# init(UIEdgeInsets:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified UIKit edge insets structure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(UIEdgeInsets insets: UIEdgeInsets)
```

```swift
init(uiEdgeInsets insets: UIEdgeInsets)
```

```objc
+ (NSValue *) valueWithUIEdgeInsets:(UIEdgeInsets) insets;
```

#### Return Value

A new value object that contains the edge inset information.

## Parameters

- `insets`: The value for the new object.

## See Also

### Related Documentation
- [struct UIEdgeInsets](../../UIKit/uiedgeinsets.md)
  The inset distances for views.
### Working with UIKit Geometry Values
- [init(UIOffset: UIOffset)](./init%28uioffset%29.md)
  Creates a new value object containing the specified UIKit offset structure.
- [var uiEdgeInsetsValue: UIEdgeInsets](./uiedgeinsetsvalue.md)
  Returns the UIKit edge insets structure representation of the value.
- [var uiOffsetValue: UIOffset](./uioffsetvalue.md)
  Returns the UIKit offset structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(uiedgeinsets:))*