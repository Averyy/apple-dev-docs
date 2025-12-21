# NSEqualRanges(_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a Boolean value that indicates whether two given ranges are equal.

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
func NSEqualRanges(_ range1: NSRange, _ range2: NSRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `range1` and `range2` have the same locations and lengths.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsequalranges(_:_:))*