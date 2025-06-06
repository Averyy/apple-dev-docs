# init(repeating:count:)

**Framework**: MusicKit  
**Kind**: init

Creates a new collection containing the specified number of a single, repeated value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/init(repeating:count:))*