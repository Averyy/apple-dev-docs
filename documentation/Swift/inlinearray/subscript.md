# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
subscript(i: InlineArray<count, Element>.Index) -> Element { get set }
```

#### Overview

> **Note**: O(1)

## Parameters

- `i`: The position of the element to access.   must be a valid   index of the array that is not equal to the   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/subscript(_:))*