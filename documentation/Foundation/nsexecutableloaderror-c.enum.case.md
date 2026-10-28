# NSExecutableLoadError

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

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

```c
NSExecutableLoadError
```

## Discussion

This error covers situations such as an error caused by a library the executable depends on.

## See Also

### Errors
- [NSExecutableErrorMinimum](./nsexecutableerrorminimum-c.enum.case.md)
  The beginning of the range of error codes reserved for errors related to executable files.
- [NSExecutableNotLoadableError](./nsexecutablenotloadableerror-c.enum.case.md)
  The executable type isn’t loadable in the current process.
- [NSExecutableArchitectureMismatchError](./nsexecutablearchitecturemismatcherror-c.enum.case.md)
  The executable doesn’t provide an architecture compatible with the current process.
- [NSExecutableRuntimeMismatchError](./nsexecutableruntimemismatcherror-c.enum.case.md)
  The executable has Objective-C runtime information that’s incompatible with the current process.
- [NSExecutableLinkError](./nsexecutablelinkerror-c.enum.case.md)
  The executable failed due to linking issues.
- [NSExecutableErrorMaximum](./nsexecutableerrormaximum-c.enum.case.md)
  The end of the range of error codes reserved for errors related to executable files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexecutableloaderror-c.enum.case)*