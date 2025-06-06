# contains(_:)

**Framework**: TabularData  
**Kind**: method

Returns a Boolean value indicating whether the sequence contains the given element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/contains(_:)-2l8hr)*