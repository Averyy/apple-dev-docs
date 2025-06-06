# subarray(with:)

**Framework**: Foundation  
**Kind**: method

Returns a new array containing the receiving array’s elements that fall within the limits specified by a given range.

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
func subarray(with range: NSRange) -> [Any]
```

#### Return Value

A new array containing the receiving array’s elements that fall within the limits specified by `range`.

#### Discussion

If `range` isn’t within the receiving array’s range of elements, an `NSRangeException` is raised.

For example, the following code example creates an array containing the elements found in the first half of `wholeArray` (assuming `wholeArray` exists).

```objc
NSArray *halfArray;
NSRange theRange;
 
theRange.location = 0;
theRange.length = [wholeArray count] / 2;
 
halfArray = [wholeArray subarrayWithRange:theRange];
```

## Parameters

- `range`: A range within the receiving array’s range of elements.

## See Also

- [func adding(Any) -> [Any]](nsarray/adding(_:).md)
  Returns a new array that is a copy of the receiving array with a given object added to the end.
- [func addingObjects(from: [Any]) -> [Any]](nsarray/addingobjects(from:).md)
  Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [func filtered(using: NSPredicate) -> [Any]](nsarray/filtered(using:).md)
  Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/subarray(with:))*