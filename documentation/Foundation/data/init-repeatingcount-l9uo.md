# init(repeating:count:)

**Framework**: Foundation  
**Kind**: init

Creates a new collection containing the specified number of a single, repeated value.

**Availability**:
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(repeating repeatedValue: Self.Element, count: Int)
```

#### Discussion

Here’s an example of creating an array initialized with five strings containing the letter .

```None
let fiveZs = Array(repeating: "Z", count: 5)
print(fiveZs)
// Prints "["Z", "Z", "Z", "Z", "Z"]"
```

## Parameters

- `repeatedValue`: The element to repeat.
- `count`: The number of times to repeat the value passed in the    parameter.   must be zero or greater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(repeating:count:)-l9uo)*