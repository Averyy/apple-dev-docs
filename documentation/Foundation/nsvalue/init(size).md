# init(size:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified Foundation size structure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(size: NSSize)
```

```objc
+ (NSValue *) valueWithSize:(NSSize) size;
```

#### Return Value

A new value object that contains the size information.

## Parameters

- `size`: The value for the new object.

## See Also

### Related Documentation
- [typealias NSSize](../nssize.md)
  A two-dimensional size.
### Working with Foundation Geometry Values
- [init(point: NSPoint)](./init%28point%29.md)
  Creates a new value object containing the specified Foundation point structure.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates a new value object containing the specified Foundation rectangle structure.
- [var pointValue: NSPoint](./pointvalue.md)
  The Foundation point structure representation of the value.
- [var sizeValue: NSSize](./sizevalue.md)
  The Foundation size structure representation of the value.
- [var rectValue: NSRect](./rectvalue.md)
  The Foundation rectangle structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(size:))*