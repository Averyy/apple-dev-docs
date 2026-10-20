# withUnsafeBytes(for:_:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Call a function and pass a buffer representing this instance to it.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
borrowing func withUnsafeBytes<R>(for attachment: borrowing Attachment<Self>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```

## Mentions

- [Migrating a test from XCTest](../migratingfromxctest.md)

#### Return Value

Whatever is returned by `body`.

#### Discussion

> **Throws**: Whatever is thrown by `body`, or any error that prevented the creation of the buffer.

The testing library uses this function when saving an attachment. The format of the buffer is implementation-defined, but should be “idiomatic” for this type: for example, if this type represents an image, it would be appropriate for the buffer to contain an image in PNG format, JPEG format, etc., but it would not be idiomatic for the buffer to contain a textual description of the image.

## Parameters

- `attachment`: The attachment that is requesting a buffer (that is, the attachment containing this instance.)
- `body`: A function to call. A temporary buffer containing a data representation of this instance is passed to it.

## Default Implementations

### Attachable Implementations
- [func withUnsafeBytes<R>(for: borrowing Attachment<Self>, (UnsafeRawBufferPointer) throws -> R) throws -> R](./withunsafebytes%28for,_%29-4m3s9.md)
  Encode this value into a buffer using either [PropertyListEncoder](../../Foundation/propertylistencoder.md) or [JSONEncoder](../../Foundation/jsonencoder.md), then call a function and pass that buffer to it.
- [func withUnsafeBytes<R>(for: borrowing Attachment<Self>, (UnsafeRawBufferPointer) throws -> R) throws -> R](./withunsafebytes%28for,_%29-8ied9.md)
  Encode this object using [NSKeyedArchiver](../../Foundation/nskeyedarchiver.md) into a buffer, then call a function and pass that buffer to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachable/withunsafebytes(for:_:))*