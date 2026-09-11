# remove(at:)

**Framework**: Swift  
**Kind**: method

Removes and returns the element at the specified position.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
mutating func remove(at index: Int) -> Element
```

#### Return Value

The removed element.

#### Discussion

All the elements following the specified position are moved to close the gap.

> **Note**: O(`self.count`)

## Parameters

- `index`: The position of the element to remove. `index` must be a valid index of the array that is not equal to the end index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/remove(at:))*