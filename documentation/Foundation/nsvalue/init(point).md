# init(point:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified Foundation point structure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(point: NSPoint)
```

```objc
+ (NSValue *) valueWithPoint:(NSPoint) point;
```

#### Return Value

A new value object that contains the point information.

## Parameters

- `point`: The value for the new object.

## See Also

### Related Documentation
- [typealias NSPoint](../nspoint.md)
  A point in a Cartesian coordinate system.
### Working with Foundation Geometry Values
- [init(size: NSSize)](./init%28size%29.md)
  Creates a new value object containing the specified Foundation size structure.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates a new value object containing the specified Foundation rectangle structure.
- [var pointValue: NSPoint](./pointvalue.md)
  The Foundation point structure representation of the value.
- [var sizeValue: NSSize](./sizevalue.md)
  The Foundation size structure representation of the value.
- [var rectValue: NSRect](./rectvalue.md)
  The Foundation rectangle structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(point:))*