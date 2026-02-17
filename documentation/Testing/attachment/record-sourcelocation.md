# record(_:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: method

Attach an attachment to the current test.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
static func record(_ attachment: consuming Attachment<AttachableValue>, sourceLocation: SourceLocation = #_sourceLocation)
```

#### Discussion

When `attachableValue` is an instance of a type that does not conform to the [`Sendable`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/sendable) protocol, the testing library calls its [`withUnsafeBytes(for:_:)`](attachable/withunsafebytes(for:_:).md) immediately and records a copy of the resulting buffer instead. If `attachableValue` throws an error when the testing library calls its [`withUnsafeBytes(for:_:)`](attachable/withunsafebytes(for:_:).md) function, the testing library records that error as an issue in the current test.

## Parameters

- `attachment`: The attachment to attach.
- `sourceLocation`: The source location of the call to this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/record(_:sourcelocation:))*