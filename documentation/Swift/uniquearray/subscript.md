# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position.

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
subscript(position: Int) -> Element { borrow mutate }
```

#### Overview

> **Note**: O(1)

## Parameters

- `position`: The position of the element to access. The position must be a valid index of the array that is not equal to the `endIndex` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/subscript(_:))*