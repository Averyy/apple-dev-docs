# moveElement(from:)

**Framework**: Swift  
**Kind**: method

Retrieves and returns the element at `index`, leaving that element’s underlying memory uninitialized.

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
func moveElement<Element>(from index: Slice<Base>.Index) -> Element where Base == UnsafeMutableBufferPointer<Element>
```

#### Return Value

The instance referenced by this index in this buffer.

#### Discussion

The memory underlying the element at `index` must be initialized. After calling `moveElement(from:)`, the memory underlying this element of the buffer slice is uninitialized, and still bound to type `Element`.

## Parameters

- `index`: The index of the buffer element to retrieve and deinitialize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/moveelement(from:))*