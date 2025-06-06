# execFormatError

**Framework**: System  
**Kind**: property

Executable format error.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var execFormatError: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A request was made to execute a file that, although it has the appropriate permissions, isn’t in the format required for an executable file.

The corresponding C error is `ENOEXEC`.

## See Also

- [static var badCPUType: Errno](errno/badcputype.md)
  Bad CPU type in executable.
- [static var badExecutable: Errno](errno/badexecutable.md)
  Bad executable or shared library.
- [static var malformedMachO: Errno](errno/malformedmacho.md)
  Malformed Mach-O file.
- [static var sharedLibraryVersionMismatch: Errno](errno/sharedlibraryversionmismatch.md)
  Shared library version mismatch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/execformaterror)*