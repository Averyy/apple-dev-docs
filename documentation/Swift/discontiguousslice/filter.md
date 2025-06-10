# filter(_:)

**Framework**: Swift  
**Kind**: method

Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func filter(_ isIncluded: (Self.Element) throws -> Bool) rethrows -> [Self.Element]
```

#### Return Value

An array of the elements that `isIncluded` allowed.

#### Discussion

In this example, `filter(_:)` is used to include only names shorter than five characters.

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let shortNames = cast.filter { $0.count < 5 }
print(shortNames)
// Prints "["Kim", "Karl"]"
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `isIncluded`: A closure that takes an element of the   sequence as its argument and returns a Boolean value indicating   whether the element should be included in the returned array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice/filter(_:))*