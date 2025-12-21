# init(_:named:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: init

Initialize an instance of this type that encloses the given attachable value.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
init(_ attachableValue: consuming AttachableValue, named preferredName: String? = nil, sourceLocation: SourceLocation = #_sourceLocation)
```

## Parameters

- `attachableValue`: The value that will be attached to the output of the   test run.
- `preferredName`: The preferred name of the attachment when writing it to   a test report or to disk. If  , the testing library attempts to   derive a reasonable filename for the attached value.
- `sourceLocation`: The source location of the call to this initializer.   This value is used when recording issues associated with the   attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/init(_:named:sourcelocation:))*