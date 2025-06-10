# withUnsafeBytes(for:_:)

**Framework**: Foundation  
**Kind**: method

Encode this value into a buffer using either [`PropertyListEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/propertylistencoder) or [`JSONEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/jsonencoder), then call a function and pass that buffer to it.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
func withUnsafeBytes<R>(for attachment: borrowing Attachment<Self>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```

#### Return Value

Whatever is returned by `body`.

#### Discussion

> **Note**: Whatever is thrown by `body`, or any error that prevented the creation of the buffer.

The testing library uses this function when writing an attachment to a test report or to a file on disk. The encoding used depends on the path extension specified by the value of `attachment`’s `Testing/Attachment/preferredName` property:

| Extension | Encoding Used | Encoder Used |
| --- | --- | --- |
| `".xml"` | XML property list | [`PropertyListEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/propertylistencoder) |
| `".plist"` | Binary property list | [`PropertyListEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/propertylistencoder) |
| None, `".json"` | JSON | [`JSONEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/jsonencoder) |

OpenStep-style property lists are not supported. If a value conforms to  [`Encodable`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/encodable)  [`NSSecureCoding`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/nssecurecoding), the default implementation of this function uses the value’s conformance to `Encodable`.

## Parameters

- `attachment`: The attachment that is requesting a buffer (that is, the   attachment containing this instance.)
- `body`: A function to call. A temporary buffer containing a data   representation of this instance is passed to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/withunsafebytes(for:_:)-bpji)*