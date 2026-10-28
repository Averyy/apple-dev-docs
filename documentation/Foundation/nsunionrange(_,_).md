# NSUnionRange(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns the union of the specified ranges.

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
func NSUnionRange(_ range1: NSRange, _ range2: NSRange) -> NSRange
```

```c
extern NSRange NSUnionRange(NSRange range1, NSRange range2);
```

## Return Value

A range covering all indices in and between `range1` and `range2`. If one range is completely contained in the other, the returned range is equal to the larger range.

## See Also

### Managing ranges
- [func NSEqualRanges(NSRange, NSRange) -> Bool](./nsequalranges%28_,_%29.md)
  Returns a Boolean value that indicates whether two given ranges are equal.
- [func NSIntersectionRange(NSRange, NSRange) -> NSRange](./nsintersectionrange%28_,_%29.md)
  Returns the intersection of the specified ranges.
- [func NSLocationInRange(Int, NSRange) -> Bool](./nslocationinrange%28_,_%29.md)
  Returns a Boolean value that indicates whether a specified position is in a given range.
- [func NSMakeRange(Int, Int) -> NSRange](./nsmakerange%28_,_%29.md)
  Creates a new NSRange from the specified values.
- [func NSMaxRange(NSRange) -> Int](./nsmaxrange%28_%29.md)
  Returns the sum of the location and length of the range.
- [func NSRangeFromString(String) -> NSRange](./nsrangefromstring%28_%29.md)
  Returns a range from a textual representation.
- [func NSStringFromRange(NSRange) -> String](./nsstringfromrange%28_%29.md)
  Returns a string representation of a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunionrange(_:_:))*