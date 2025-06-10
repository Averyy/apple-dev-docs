# NSRange

**Framework**: Foundation  
**Kind**: typealias

A structure used to describe a portion of a series, such as characters in a string or objects in an array.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias NSRange = _NSRange
```

#### Discussion

Foundation functions that operate on ranges include the following:

- [`NSEqualRanges(_:_:)`](nsequalranges(_:_:).md)
- [`NSIntersectionRange(_:_:)`](nsintersectionrange(_:_:).md)
- [`NSLocationInRange(_:_:)`](nslocationinrange(_:_:).md)
- [`NSMakeRange(_:_:)`](nsmakerange(_:_:).md)
- [`NSMaxRange(_:)`](nsmaxrange(_:).md)
- [`NSRangeFromString(_:)`](nsrangefromstring(_:).md)
- [`NSStringFromRange(_:)`](nsstringfromrange(_:).md)
- [`NSUnionRange(_:_:)`](nsunionrange(_:_:).md)

## Topics

### Creating a range
- [init()](nsrange-swift.typealias/init.md)
  Creates an empty range.
- [init(location: Int, length: Int)](nsrange-swift.typealias/init(location:length:).md)
  Creates a range with the given location and length.
### Accessing range properties
- [var location: Int](nsrange-swift.typealias/location.md)
  The index of the first member of the range.
- [var length: Int](nsrange-swift.typealias/length.md)
  The number of items in the range.
### Managing ranges
- [func NSEqualRanges(NSRange, NSRange) -> Bool](nsequalranges(_:_:).md)
  Returns a Boolean value that indicates whether two given ranges are equal.
- [func NSIntersectionRange(NSRange, NSRange) -> NSRange](nsintersectionrange(_:_:).md)
  Returns the intersection of the specified ranges.
- [func NSLocationInRange(Int, NSRange) -> Bool](nslocationinrange(_:_:).md)
  Returns a Boolean value that indicates whether a specified position is in a given range.
- [func NSMakeRange(Int, Int) -> NSRange](nsmakerange(_:_:).md)
  Creates a new NSRange from the specified values.
- [func NSMaxRange(NSRange) -> Int](nsmaxrange(_:).md)
  Returns the sum of the location and length of the range.
- [func NSRangeFromString(String) -> NSRange](nsrangefromstring(_:).md)
  Returns a range from a textual representation.
- [func NSStringFromRange(NSRange) -> String](nsstringfromrange(_:).md)
  Returns a string representation of a range.
- [func NSUnionRange(NSRange, NSRange) -> NSRange](nsunionrange(_:_:).md)
  Returns the union of the specified ranges.
### Related types
- [typealias NSRangePointer](nsrangepointer.md)
  Type indicating a parameter is a pointer to an `NSRange` structure.
- [let NSNotFound: Int](nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrange-swift.typealias)*