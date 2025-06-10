# Attachments

**Framework**: Swift Testing

Attach values to tests to help diagnose issues and gather feedback.

#### Overview

Attach values such as strings and files to tests.  Implement the [`Attachable`](attachable.md) protocol to create your own attachable types.

## Topics

### Attaching values to tests
- [struct Attachment](attachment.md)
  A type describing values that can be attached to the output of a test run and inspected later by the user.
- [protocol Attachable](attachable.md)
  A protocol describing a type that can be attached to a test report or written to disk when a test is run.
- [protocol AttachableWrapper](attachablewrapper.md)
  A protocol describing a type that can be attached to a test report or written to disk when a test is run and which contains another value that it stands in for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachments)*