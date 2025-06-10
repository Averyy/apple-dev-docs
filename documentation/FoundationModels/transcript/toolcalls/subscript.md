# subscript(_:)

**Framework**: Foundation Models  
**Kind**: subscript

Accesses the element at the specified position.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
subscript(position: Int) -> Transcript.ToolCall { get }
```

#### Overview

The following example accesses an element of an array through its subscript to print its value:

```None
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
print(streets[1])
// Prints "Bryant"
```

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

> **Note**: O(1)

## Parameters

- `position`: The position of the element to access.    must be a valid index of the collection that is not equal to the    property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/subscript(_:))*