# contains(_:)

**Framework**: SwiftData  
**Kind**: method

Returns a Boolean value indicating whether the sequence contains the given element.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func contains(_ element: Self.Element) -> Bool
```

#### Return Value

`true` if the element was found in the sequence; otherwise, `false`.

#### Discussion

This example checks to see whether a favorite actor is in an array storing a movie’s cast.

```swift
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchresultscollection/contains(_:)-12nlj)*