# NSLocationInRange(_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a specified position is in a given range.

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
func NSLocationInRange(_ loc: Int, _ range: NSRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `loc` lies within `range`—that is, if it’s greater than or equal to `range.location` and less than `range.location` plus `range.length`.

## See Also

- [func NSEqualRanges(NSRange, NSRange) -> Bool](nsequalranges(_:_:).md)
  Returns a Boolean value that indicates whether two given ranges are equal.
- [func NSIntersectionRange(NSRange, NSRange) -> NSRange](nsintersectionrange(_:_:).md)
  Returns the intersection of the specified ranges.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocationinrange(_:_:))*