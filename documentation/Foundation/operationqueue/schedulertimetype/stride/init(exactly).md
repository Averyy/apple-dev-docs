# init(exactly:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a stride using the specified integer, if it can be represented exactly.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init?<T>(exactly source: T) where T : BinaryInteger
```

## See Also

### Creating Scheduler Time Strides
- [init(TimeInterval)](./init%28_%29.md)
  Creates a stride using the specified time interval.
- [init(floatLiteral: TimeInterval)](./init%28floatliteral%29.md)
  Creates a stride using the specified floating-point value.
- [init(integerLiteral: TimeInterval)](./init%28integerliteral%29.md)
  Creates a stride using the specified integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/stride/init(exactly:))*