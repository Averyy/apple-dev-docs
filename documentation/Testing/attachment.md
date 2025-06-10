# Attachment

**Framework**: Swift Testing  
**Kind**: struct

A type describing values that can be attached to the output of a test run and inspected later by the user.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
struct Attachment<AttachableValue> where AttachableValue : Attachable, AttachableValue : ~Copyable
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)

#### Overview

Attachments are included in test reports in Xcode or written to disk when tests are run at the command line. To create an attachment, you need a value of some type that conforms to [`Attachable`](attachable.md). Initialize an instance of [`Attachment`](attachment.md) with that value and, optionally, a preferred filename to use when writing to disk.

## Topics

### Initializers
- [init(consuming AttachableValue, named: String?, sourceLocation: SourceLocation)](attachment/init(_:named:sourcelocation:).md)
  Initialize an instance of this type that encloses the given attachable value.
- [init(contentsOf: URL, named: String?, sourceLocation: SourceLocation) async throws](attachment/init(contentsof:named:sourcelocation:).md)
  Initialize an instance of this type with the contents of the given URL.
### Instance Properties
- [var attachableValue: AttachableValue](attachment/attachablevalue-2tnj5.md)
  The value of this attachment.
- [var attachableValue: AttachableValue.Wrapped](attachment/attachablevalue-vkrw.md)
  The value of this attachment.
- [var preferredName: String](attachment/preferredname.md)
  A filename to use when writing this attachment to a test report or to a file on disk.
### Instance Methods
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) throws -> R](attachment/withunsafebytes(_:).md)
  Call a function and pass a buffer representing the value of this instance’s [`attachableValue`](attachment/attachablevalue-2tnj5.md) property to it.
### Type Methods
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Attachable](attachable.md)
  A protocol describing a type that can be attached to a test report or written to disk when a test is run.
- [protocol AttachableWrapper](attachablewrapper.md)
  A protocol describing a type that can be attached to a test report or written to disk when a test is run and which contains another value that it stands in for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment)*