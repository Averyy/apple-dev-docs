# contains(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value indicating whether the sequence contains the given element.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func contains(_ element: Self.Element) -> Bool
```

#### Return Value

`true` if the element was found in the sequence; otherwise, `false`.

#### Discussion

This example checks to see whether a favorite actor is in an array storing a movie’s cast.

```None
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
print(cast.contains("Marlon"))
// Prints "true"
print(cast.contains("James"))
// Prints "false"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `element`: The element to find in the sequence.

## See Also

- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](queryresult/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](queryresult/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](queryresult/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/contains(_:))*