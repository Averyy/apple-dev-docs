# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at specified position.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
subscript(position: Range<Bound>.Index) -> Range<Bound>.Element { get }
```

#### Overview

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

## Parameters

- `position`: The position of the element to access.    must be a valid index of the range, and must not equal the range’s end   index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/subscript(_:)-84ykx)*