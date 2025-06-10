# Attachable Implementations

**Framework**: Foundation

## Topics

### Instance Methods
- [func preferredName(for: borrowing Attachment<Self>, basedOn: String) -> String](data/preferredname(for:basedon:).md)
  Generate a preferred name for the given attachment.
- [func withUnsafeBytes<R>(for: borrowing Attachment<Data>, (UnsafeRawBufferPointer) throws -> R) throws -> R](data/withunsafebytes(for:_:).md)
- [func withUnsafeBytes<R>(for: borrowing Attachment<Self>, (UnsafeRawBufferPointer) throws -> R) throws -> R](data/withunsafebytes(for:_:)-bpji.md)
  Encode this value into a buffer using either [`PropertyListEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/propertylistencoder) or [`JSONEncoder`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/jsonencoder), then call a function and pass that buffer to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/attachable-implementations)*