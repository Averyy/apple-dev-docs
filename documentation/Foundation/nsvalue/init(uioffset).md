# init(UIOffset:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified UIKit offset structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(UIOffset insets: UIOffset)
```

```swift
init(uiOffset insets: UIOffset)
```

```objc
+ (NSValue *) valueWithUIOffset:(UIOffset) insets;
```

## Return Value

A new value object that contains the offset information.

## Parameters

- `insets`: The value for the new object.

## See Also

### Related Documentation
- [struct UIOffset](../../UIKit/uioffset.md)
  A structure that specifies an amount to offset a position.
### Working with UIKit Geometry Values
- [init(UIEdgeInsets: UIEdgeInsets)](./init%28uiedgeinsets%29.md)
  Creates a new value object containing the specified UIKit edge insets structure.
- [var uiEdgeInsetsValue: UIEdgeInsets](./uiedgeinsetsvalue.md)
  Returns the UIKit edge insets structure representation of the value.
- [var uiOffsetValue: UIOffset](./uioffsetvalue.md)
  Returns the UIKit offset structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(uioffset:))*