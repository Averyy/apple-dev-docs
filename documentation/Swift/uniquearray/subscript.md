# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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