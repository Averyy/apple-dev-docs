# initializeElement(at:to:)

**Framework**: Swift  
**Kind**: method

Initializes the element at `index` to the given value.

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
func initializeElement<Element>(at index: Int, to value: Element) where Base == UnsafeMutableBufferPointer<Element>
```

#### Discussion

The memory underlying the destination element must be uninitialized, or `Element` must be a trivial type. After a call to `initialize(to:)`, the memory underlying this element of the buffer slice is initialized.

## Parameters

- `index`: The index of the element to initialize
- `value`: The value used to initialize the buffer element’s memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/initializeelement(at:to:))*