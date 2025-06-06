# initialize(repeating:)

**Framework**: Swift  
**Kind**: method

Initializes every element in this buffer slice’s memory to a copy of the given value.

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
func initialize<Element>(repeating repeatedValue: Element) where Base == UnsafeMutableBufferPointer<Element>
```

#### Discussion

The destination memory must be uninitialized or the buffer’s `Element` must be a trivial type. After a call to `initialize(repeating:)`, the entire region of memory referenced by this buffer slice is initialized.

## Parameters

- `repeatedValue`: The value with which to initialize this   buffer slice’s memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/initialize(repeating:))*