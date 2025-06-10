# record(_:named:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: method

Attach a value to the current test.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
static func record(_ attachableValue: consuming AttachableValue, named preferredName: String? = nil, sourceLocation: SourceLocation = #_sourceLocation)
```

#### Discussion

When attaching a value of a type that does not conform to both [`Sendable`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/sendable) and [`Copyable`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/copyable), the testing library encodes it as data immediately. If the value cannot be encoded and an error is thrown, that error is recorded as an issue in the current test and the attachment is not written to the test report or to disk.

This function creates a new instance of [`Attachment`](attachment.md) and immediately attaches it to the current test.

An attachment can only be attached once.

## Parameters

- `attachableValue`: The value to attach.
- `preferredName`: The preferred name of the attachment when writing it to   a test report or to disk. If  , the testing library attempts to   derive a reasonable filename for the attached value.
- `sourceLocation`: The source location of the call to this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/record(_:named:sourcelocation:))*