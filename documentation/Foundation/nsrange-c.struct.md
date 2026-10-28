# NSRange

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef struct _NSRange { ... } NSRange;
```

## Discussion

Foundation functions that operate on ranges include the following:

- [`NSEqualRanges(_:_:)`](./nsequalranges%28_,_%29.md)
- [`NSIntersectionRange(_:_:)`](./nsintersectionrange%28_,_%29.md)
- [`NSLocationInRange(_:_:)`](./nslocationinrange%28_,_%29.md)
- [`NSMakeRange(_:_:)`](./nsmakerange%28_,_%29.md)
- [`NSMaxRange(_:)`](./nsmaxrange%28_%29.md)
- [`NSRangeFromString(_:)`](./nsrangefromstring%28_%29.md)
- [`NSStringFromRange(_:)`](./nsstringfromrange%28_%29.md)
- [`NSUnionRange(_:_:)`](./nsunionrange%28_,_%29.md)

## Topics

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
- [func NSUnionRange(NSRange, NSRange) -> NSRange](./nsunionrange%28_,_%29.md)
  Returns the union of the specified ranges.
### Related types
- [typealias NSRangePointer](./nsrangepointer.md)
  Type indicating a parameter is a pointer to an `NSRange` structure.
- [var NSNotFound: Int](./nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.
### Instance Properties
- [length](./nsrange-c.struct/length.md)
- [location](./nsrange-c.struct/location.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrange-c.struct)*