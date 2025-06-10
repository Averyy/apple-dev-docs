# subscript(_:)

**Framework**: SwiftData  
**Kind**: subscript

Accesses the element at the specified position.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
subscript(position: Int) -> Element { get }
```

#### Overview

The following example accesses an element of an array through its subscript to print its value:

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
print(streets[1])
// Prints "Bryant"
```

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

> **Note**: O(1)

## Parameters

- `position`: The position of the element to access.    must be a valid index of the collection that is not equal to the    property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchresultscollection/subscript(_:))*