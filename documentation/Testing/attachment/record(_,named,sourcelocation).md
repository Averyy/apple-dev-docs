# record(_:named:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Type Method

Attach a value to the current test.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
static func record(_ attachableValue: consuming AttachableValue, named preferredName: String? = nil, sourceLocation: SourceLocation = #_sourceLocation)
```

Available when `AttachableValue` conforms to `Attachable`.

#### Discussion

When `attachableValue` is an instance of a type that does not conform to the [Sendable](../../Swift/sendable.md) protocol, the testing library calls its [`withUnsafeBytes(for:_:)`](../attachable/withunsafebytes%28for,_%29.md) immediately and records a copy of the resulting buffer instead. If `attachableValue` throws an error when the testing library calls its [`withUnsafeBytes(for:_:)`](../attachable/withunsafebytes%28for,_%29.md) function, the testing library records that error as an issue in the current test.

This function creates a new instance of [`Attachment`](../attachment.md) and immediately attaches it to the current test.

## Parameters

- `attachableValue`: The value to attach.
- `preferredName`: The preferred name of the attachment to use when saving it. If `nil`, the testing library attempts to generate a reasonable filename for the attached value.
- `sourceLocation`: The source location of the call to this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/record(_:named:sourcelocation:))*