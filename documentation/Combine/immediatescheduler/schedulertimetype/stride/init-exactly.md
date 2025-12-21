# init(exactly:)

**Framework**: Combine  
**Kind**: init

Creates an immediate scheduler time interval from a binary integer type.

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

#### Discussion

If `exactly` can’t convert to an `Int`, the resulting time interval is `nil`.

## See Also

- [init(Int)](immediatescheduler/schedulertimetype/stride/init(_:).md)
  Creates an immediate scheduler time interval from the given time interval.
- [init(floatLiteral: Double)](immediatescheduler/schedulertimetype/stride/init(floatliteral:).md)
  Creates an immediate scheduler time interval from a floating-point seconds value.
- [init(integerLiteral: Int)](immediatescheduler/schedulertimetype/stride/init(integerliteral:).md)
  Creates an immediate scheduler time interval from an integer seconds value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride/init(exactly:))*