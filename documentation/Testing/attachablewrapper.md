# AttachableWrapper

**Framework**: Swift Testing  
**Kind**: protocol

A protocol describing a type that can be attached to a test report or written to disk when a test is run and which contains another value that it stands in for.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
protocol AttachableWrapper<Wrapped> : Attachable, ~Copyable
```

#### Overview

To attach an attachable value to a test, pass it to [`record(_:named:sourceLocation:)`](attachment/record(_:named:sourcelocation:).md). To further configure an attachable value before you attach it, use it to initialize an instance of [`Attachment`](attachment.md) and set its properties before passing it to [`record(_:sourceLocation:)`](attachment/record(_:sourcelocation:).md). An attachable value can only be attached to a test once.

A type can conform to this protocol if it represents another type that cannot directly conform to [`Attachable`](attachable.md), such as a non-final class or a type declared in a third-party module.

## Topics

### Associated Types
- [associatedtype Wrapped](attachablewrapper/wrapped.md)
  The type of the underlying value represented by this type.
### Instance Properties
- [var wrappedValue: Self.Wrapped](attachablewrapper/wrappedvalue.md)
  The underlying value represented by this instance.

## Relationships

### Inherits From
- [Attachable](attachable.md)

## See Also

- [struct Attachment](attachment.md)
  A type describing values that can be attached to the output of a test run and inspected later by the user.
- [protocol Attachable](attachable.md)
  A protocol describing a type that can be attached to a test report or written to disk when a test is run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachablewrapper)*