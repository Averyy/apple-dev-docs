# standardOutputContent

**Framework**: Swift Testing  
**Kind**: property

All bytes written to the standard output stream of the exit test before it exited.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
var standardOutputContent: [UInt8]
```

#### Discussion

The value of this property may contain any arbitrary sequence of bytes, including sequences that are not valid UTF-8 and cannot be decoded by [`String.init(cString:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/string/init(cstring:)-6kr8s). Consider using [`String.init(validatingCString:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/string/init(validatingcstring:)-992vo) instead.

When checking the value of this property, keep in mind that the standard output stream is globally accessible, and any code running in an exit test may write to it including including the operating system and any third-party dependencies you have declared in your package. Rather than comparing the value of this property with [`==`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/array/==(_:_:)), use [`contains(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/collection/contains(_:)) to check if expected output is present.

To enable gathering output from the standard output stream during an exit test, pass `\.standardOutputContent` in the `observedValues` argument of [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](expect(processexitswith:observing:_:sourcelocation:performing:).md) or [`require(processExitsWith:observing:_:sourceLocation:performing:)`](require(processexitswith:observing:_:sourcelocation:performing:).md).

If you did not request standard output content when running an exit test, the value of this property is the empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/result/standardoutputcontent)*