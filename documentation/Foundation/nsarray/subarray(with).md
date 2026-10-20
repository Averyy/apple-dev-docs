# subarray(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<id> *) subarrayWithRange:(NSRange) range;
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

### Deriving New Arrays
- [func adding(Any) -> [Any]](./adding%28_%29.md)
  Returns a new array that is a copy of the receiving array with a given object added to the end.
- [func addingObjects(from: [Any]) -> [Any]](./addingobjects%28from%29.md)
  Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [func filtered(using: NSPredicate) -> [Any]](./filtered%28using%29.md)
  Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/subarray(with:))*