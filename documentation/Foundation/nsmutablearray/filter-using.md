# filter(using:)

**Framework**: Foundation  
**Kind**: method

Evaluates a given predicate against the array’s content and leaves only objects that match.

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
func filter(using predicate: NSPredicate)
```

## Parameters

- `predicate`: The predicate to evaluate against the array’s elements.

## See Also

- [func filtered(using: NSPredicate) -> [Any]](nsarray/filtered(using:).md)
  Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/filter(using:))*