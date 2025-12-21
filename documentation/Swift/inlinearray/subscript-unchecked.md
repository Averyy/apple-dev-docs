# subscript(unchecked:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
subscript(unchecked i: InlineArray<count, Element>.Index) -> Element { get set }
```

#### Overview

> ⚠️ **Warning**: This subscript trades safety for performance. Using an invalid index results in undefined behavior.

> **Note**: O(1)

## Parameters

- `i`: The position of the element to access.   must be a valid   index of the array that is not equal to the   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/subscript(unchecked:))*