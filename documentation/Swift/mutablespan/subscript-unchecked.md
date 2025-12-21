# subscript(unchecked:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position in the `Span`.

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
subscript(unchecked position: MutableSpan<Element>.Index) -> Element { get set }
```

#### Overview

This subscript does not validate `position`; this is an unsafe operation.

> **Note**: O(1)

## Parameters

- `position`: The offset of the element to access.    must be greater or equal to zero, and less than  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan/subscript(unchecked:))*