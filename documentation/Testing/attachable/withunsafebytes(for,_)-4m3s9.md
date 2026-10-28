# withUnsafeBytes(for:_:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Instance Method

Encode this value into a buffer using either [PropertyListEncoder](../../Foundation/propertylistencoder.md) or [JSONEncoder](../../Foundation/jsonencoder.md), then call a function and pass that buffer to it.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
func withUnsafeBytes<R>(for attachment: borrowing Attachment<Self>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```

Available when `Self` conforms to `Encodable`.

## Return Value

Whatever is returned by `body`.

## Discussion

> **Throws**: Whatever is thrown by `body`, or any error that prevented the creation of the buffer.

The testing library uses this function when writing an attachment to a test report or to a file on disk. The encoding used depends on the path extension specified by the value of `attachment`’s [`preferredName`](../attachment/preferredname.md) property:

| Extension | Encoding Used | Encoder Used |
| --- | --- | --- |
| `".xml"` | XML property list | [PropertyListEncoder](../../Foundation/propertylistencoder.md) |
| `".plist"` | Binary property list | [`PropertyListEncoder`](../../Foundation/propertylistencoder.md) |
| None, `".json"` | JSON | [JSONEncoder](../../Foundation/jsonencoder.md) |

OpenStep-style property lists are not supported. If a value conforms to *both* [Encodable](../../Swift/encodable.md) *and* [NSSecureCoding](../../Foundation/nssecurecoding.md), the default implementation of this function uses the value’s conformance to `Encodable`.

## Parameters

- `attachment`: The attachment that is requesting a buffer (that is, the attachment containing this instance.)
- `body`: A function to call. A temporary buffer containing a data representation of this instance is passed to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachable/withunsafebytes(for:_:)-4m3s9)*