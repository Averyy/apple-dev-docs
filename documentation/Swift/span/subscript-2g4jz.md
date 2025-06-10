# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position in the `Span`.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
subscript(position: Span<Element>.Index) -> Element { get }
```

#### Overview

> **Note**: O(1)

## Parameters

- `position`: The offset of the element to access.    must be greater or equal to zero, and less than  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/subscript(_:)-2g4jz)*