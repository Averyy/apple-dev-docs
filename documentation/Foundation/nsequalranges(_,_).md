# NSEqualRanges(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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

```c
static BOOL NSEqualRanges(NSRange range1, NSRange range2);
```

## Return Value

[`true`](../Swift/true.md) if `range1` and `range2` have the same locations and lengths.

## See Also

### Managing ranges
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
- [func NSUnionRange(NSRange, NSRange) -> NSRange](./nsunionrange%28_,_%29.md)
  Returns the union of the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsequalranges(_:_:))*