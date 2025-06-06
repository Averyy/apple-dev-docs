# init(repeating:count:)

**Framework**: System  
**Kind**: init

Creates a new collection containing the specified number of a single, repeated value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(repeating repeatedValue: Self.Element, count: Int)
```

#### Discussion

Here’s an example of creating an array initialized with five strings containing the letter .

```swift
let fiveZs = Array(repeating: "Z", count: 5)
print(fiveZs)
// Prints "["Z", "Z", "Z", "Z", "Z"]"
```

## Parameters

- `repeatedValue`: The element to repeat.
- `count`: The number of times to repeat the value passed in the    parameter.   must be zero or greater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/init(repeating:count:))*