# withUnsafeBytes(_:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Instance Method

Call a function and pass a buffer representing the value of this instance’s [`attachableValue`](./attachablevalue-2tnj5.md) property to it.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
borrowing func withUnsafeBytes<R>(_ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```

Available when `AttachableValue` conforms to `Attachable`.

#### Return Value

Whatever is returned by `body`.

#### Discussion

> **Throws**: Whatever is thrown by `body`, or any error that prevented the creation of the buffer.

The testing library uses this function when saving an attachment. This function calls the [`withUnsafeBytes(for:_:)`](../attachable/withunsafebytes%28for,_%29.md) function on this attachment’s [`attachableValue`](./attachablevalue-2tnj5.md) property.

## Parameters

- `body`: A function to call. A temporary buffer containing a data representation of this instance is passed to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/withunsafebytes(_:))*