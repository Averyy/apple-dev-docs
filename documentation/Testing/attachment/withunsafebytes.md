# withUnsafeBytes(_:)

**Framework**: Swift Testing  
**Kind**: method

Call a function and pass a buffer representing the value of this instance’s [`attachableValue`](attachment/attachablevalue-2tnj5.md) property to it.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
borrowing func withUnsafeBytes<R>(_ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```

#### Return Value

Whatever is returned by `body`.

#### Discussion

> **Note**: Whatever is thrown by `body`, or any error that prevented the creation of the buffer.

The testing library uses this function when writing an attachment to a test report or to a file on disk. This function calls the [`withUnsafeBytes(for:_:)`](attachable/withunsafebytes(for:_:).md) function on this attachment’s [`attachableValue`](attachment/attachablevalue-2tnj5.md) property.

## Parameters

- `body`: A function to call. A temporary buffer containing a data   representation of this instance is passed to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/withunsafebytes(_:))*