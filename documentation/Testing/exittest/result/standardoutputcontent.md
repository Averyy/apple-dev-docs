# standardOutputContent

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Instance Property

All bytes written to the standard output stream of the exit test before it exited.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
var standardOutputContent: [UInt8]
```

#### Discussion

The value of this property may contain any arbitrary sequence of bytes, including sequences that are not valid UTF-8 and cannot be decoded by [String.init(cString:)](../../../Swift/string/init%28cstring%29-6kr8s.md). Consider using [String.init(validating:as:)](../../../Swift/string/init%28validating,as%29-84qr9.md) instead.

When checking the value of this property, keep in mind that the standard output stream is globally accessible, and any code running in an exit test may write to it including the operating system and any third-party dependencies you have declared in your package. Rather than comparing the value of this property with [==](../../../Swift/array/eqeq%28_,_%29.md), use [contains(_:)](../../../Swift/collection/contains%28_%29.md) to check if expected output is present.

To enable gathering output from the standard output stream during an exit test, pass `\.standardOutputContent` in the `observedValues` argument of [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](../../expect%28processexitswith,observing,_,sourcelocation,performing%29.md) or [`require(processExitsWith:observing:_:sourceLocation:performing:)`](../../require%28processexitswith,observing,_,sourcelocation,performing%29.md).

If you did not request standard output content when running an exit test, the value of this property is the empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/result/standardoutputcontent)*