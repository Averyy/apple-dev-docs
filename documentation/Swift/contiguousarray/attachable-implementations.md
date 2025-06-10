# Attachable Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var estimatedAttachmentByteCount: Int?](contiguousarray/estimatedattachmentbytecount.md)
  An estimate of the number of bytes of memory needed to store this value as an attachment.
### Instance Methods
- [func preferredName(for: borrowing Attachment<Self>, basedOn: String) -> String](contiguousarray/preferredname(for:basedon:).md)
  Generate a preferred name for the given attachment.
- [func withUnsafeBytes<R>(for: borrowing Attachment<ContiguousArray<Element>>, (UnsafeRawBufferPointer) throws -> R) throws -> R](contiguousarray/withunsafebytes(for:_:).md)
  Call a function and pass a buffer representing this instance to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/attachable-implementations)*