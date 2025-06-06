# NSExecutableLoadError

**Framework**: Foundation  
**Kind**: var

Executable cannot be loaded for an otherwise-unspecified reason.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var NSExecutableLoadError: Int { get }
```

#### Discussion

This error covers situations such as an error caused by a library the executable depends on.

## See Also

- [var NSExecutableErrorMinimum: Int](nsexecutableerrorminimum-swift.var.md)
  The beginning of the range of error codes reserved for errors related to executable files.
- [var NSExecutableNotLoadableError: Int](nsexecutablenotloadableerror-swift.var.md)
  The executable type isn’t loadable in the current process.
- [var NSExecutableArchitectureMismatchError: Int](nsexecutablearchitecturemismatcherror-swift.var.md)
  The executable doesn’t provide an architecture compatible with the current process.
- [var NSExecutableRuntimeMismatchError: Int](nsexecutableruntimemismatcherror-swift.var.md)
  The executable has Objective-C runtime information that’s incompatible with the current process.
- [var NSExecutableLinkError: Int](nsexecutablelinkerror-swift.var.md)
  The executable failed due to linking issues.
- [var NSExecutableErrorMaximum: Int](nsexecutableerrormaximum-swift.var.md)
  The end of the range of error codes reserved for errors related to executable files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexecutableloaderror-swift.var)*