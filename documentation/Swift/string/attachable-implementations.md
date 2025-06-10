# Attachable Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var estimatedAttachmentByteCount: Int?](string/estimatedattachmentbytecount.md)
  An estimate of the number of bytes of memory needed to store this value as an attachment.
### Instance Methods
- [func preferredName(for: borrowing Attachment<Self>, basedOn: String) -> String](string/preferredname(for:basedon:).md)
  Generate a preferred name for the given attachment.
- [func withUnsafeBytes<R>(for: borrowing Attachment<String>, (UnsafeRawBufferPointer) throws -> R) throws -> R](string/withunsafebytes(for:_:).md)
  Call a function and pass a buffer representing this instance to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/attachable-implementations)*