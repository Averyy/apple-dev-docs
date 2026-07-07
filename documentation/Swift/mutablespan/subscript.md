# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified index in the `MutableSpan`.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
subscript(position: MutableSpan<Element>.Index) -> Element { borrow mutate }
```

#### Overview

> **Note**: O(1)

## Parameters

- `position`: The offset of the element to access. `position` must be greater or equal to zero, and less than `count`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan/subscript(_:))*