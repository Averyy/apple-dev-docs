# deinitializeElement(at:)

**Framework**: Swift  
**Kind**: method

Deinitializes the memory underlying the element at `index`.

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
func deinitializeElement(at index: UnsafeMutableBufferPointer<Element>.Index)
```

#### Discussion

The memory underlying the element at `index` must be initialized. After calling `deinitializeElement()`, the memory underlying this element of the buffer is uninitialized, and still bound to type `Element`.

## Parameters

- `index`: The index of the buffer element to deinitialize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/deinitializeelement(at:))*