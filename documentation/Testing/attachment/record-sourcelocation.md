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

When attaching a value of a type that does not conform to both [`Sendable`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/sendable) and [`Copyable`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/copyable), the testing library encodes it as data immediately. If the value cannot be encoded and an error is thrown, that error is recorded as an issue in the current test and the attachment is not written to the test report or to disk.

An attachment can only be attached once.

## Parameters

- `attachment`: The attachment to attach.
- `sourceLocation`: The source location of the call to this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/record(_:sourcelocation:))*