# ExitTest.Result

**Framework**: Swift Testing  
**Kind**: struct

A type representing the result of an exit test after it has exited and returned control to the calling test function.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
struct Result
```

## Mentions

- [Exit testing](exit-testing.md)

#### Overview

Both [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](expect(processexitswith:observing:_:sourcelocation:performing:).md) and [`require(processExitsWith:observing:_:sourceLocation:performing:)`](require(processexitswith:observing:_:sourcelocation:performing:).md) return instances of this type.

## Topics

### Instance Properties
- [var exitStatus: ExitStatus](exittest/result/exitstatus.md)
  The exit status reported by the process hosting the exit test.
- [var standardErrorContent: [UInt8]](exittest/result/standarderrorcontent.md)
  All bytes written to the standard error stream of the exit test before it exited.
- [var standardOutputContent: [UInt8]](exittest/result/standardoutputcontent.md)
  All bytes written to the standard output stream of the exit test before it exited.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/result)*