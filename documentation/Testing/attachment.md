# Attachment

**Framework**: Swift Testing  
**Kind**: struct

A type describing values that can be attached to the output of a test run and inspected later by the user.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
struct Attachment<AttachableValue> where AttachableValue : Attachable, AttachableValue : ~Copyable
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)

#### Overview

To create an attachment, you need a value of some type that conforms to [`Attachable`](attachable.md). Initialize an instance of [`Attachment`](attachment.md) with that value and, optionally, a preferred filename to use when saving the attachment. To record the attachment, call [`record(_:sourceLocation:)`](attachment/record(_:sourcelocation:).md). Alternatively, pass your attachable value directly to [`record(_:named:sourceLocation:)`](attachment/record(_:named:sourcelocation:).md).

## Topics

### Initializers
- [init<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](attachment/init(_:named:as:sourcelocation:).md)
  Initialize an instance of this type that encloses the given image.
- [init(consuming AttachableValue, named: String?, sourceLocation: SourceLocation)](attachment/init(_:named:sourcelocation:).md)
  Initialize an instance of this type that encloses the given attachable value.
- [init(contentsOf: URL, named: String?, sourceLocation: SourceLocation) async throws](attachment/init(contentsof:named:sourcelocation:).md)
  Initialize an instance of this type with the contents of the given URL.
- [init<T>(exporting: T, as: UTType?, named: String?, sourceLocation: SourceLocation) async throws](attachment/init(exporting:as:named:sourcelocation:).md)
  Initialize an instance of this type that encloses the given transferable value.
### Instance Properties
- [var attachableValue: AttachableValue](attachment/attachablevalue-2tnj5.md)
  The value of this attachment.
- [var attachableValue: AttachableValue.Wrapped](attachment/attachablevalue-vkrw.md)
  The value of this attachment.
- [var imageFormat: AttachableImageFormat?](attachment/imageformat.md)
  The image format to use when encoding the represented image, if specified.
- [var preferredName: String](attachment/preferredname.md)
  A filename to use when saving this attachment.
### Instance Methods
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) throws -> R](attachment/withunsafebytes(_:).md)
  Call a function and pass a buffer representing the value of this instance’s [`attachableValue`](attachment/attachablevalue-2tnj5.md) property to it.
### Type Methods
- [static func record<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](attachment/record(_:named:as:sourcelocation:).md)
  Attach an image to the current test.
- [static func record(consuming AttachableValue, named: String?, sourceLocation: SourceLocation)](attachment/record(_:named:sourcelocation:).md)
  Attach a value to the current test.
- [static func record(consuming Attachment<AttachableValue>, sourceLocation: SourceLocation)](attachment/record(_:sourcelocation:).md)
  Attach an attachment to the current test.
### Default Implementations
- [CustomStringConvertible Implementations](attachment/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Attachable](attachable.md)
  A protocol describing a type whose instances can be recorded and saved as part of a test run.
- [protocol AttachableWrapper](attachablewrapper.md)
  A protocol describing a type whose instances can be recorded and saved as part of a test run and which contains another value that it stands in for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment)*