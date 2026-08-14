# filtered(using:)

**Framework**: Foundation  
**Kind**: method

Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.

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
func filtered(using predicate: NSPredicate) -> [Any]
```

#### Return Value

A new array containing the objects in the receiving array for which `predicate` returns [`true`](https://developer.apple.com/documentation/swift/true).

Objects in the resulting array appear in the same order as they do in the receiver.

#### Discussion

For more details, see [`Predicate Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789).

## Parameters

- `predicate`: The predicate against which to evaluate the receiving array’s elements.

## See Also

- [func adding(Any) -> [Any]](nsarray/adding(_:).md)
  Returns a new array that is a copy of the receiving array with a given object added to the end.
- [func addingObjects(from: [Any]) -> [Any]](nsarray/addingobjects(from:).md)
  Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [func subarray(with: NSRange) -> [Any]](nsarray/subarray(with:).md)
  Returns a new array containing the receiving array’s elements that fall within the limits specified by a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/filtered(using:))*