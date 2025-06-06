# init(from:)

**Framework**: Combine  
**Kind**: init

Creates a new instance by decoding from the given decoder.

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
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [init(Int)](immediatescheduler/schedulertimetype/stride/init(_:).md)
  Creates an immediate scheduler time interval from the given time interval.
- [init?<T>(exactly: T)](immediatescheduler/schedulertimetype/stride/init(exactly:).md)
  Creates an immediate scheduler time interval from a binary integer type.
- [init(floatLiteral: Double)](immediatescheduler/schedulertimetype/stride/init(floatliteral:).md)
  Creates an immediate scheduler time interval from a floating-point seconds value.
- [init(integerLiteral: Int)](immediatescheduler/schedulertimetype/stride/init(integerliteral:).md)
  Creates an immediate scheduler time interval from an integer seconds value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride/init(from:))*