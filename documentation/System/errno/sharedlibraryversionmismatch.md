# sharedLibraryVersionMismatch

**Framework**: System  
**Kind**: property

Shared library version mismatch.

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
static var sharedLibraryVersionMismatch: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The version of the shared library on the system doesn’t match the expected version.

The corresponding C error is `ESHLIBVERS`.

## See Also

- [static var badCPUType: Errno](errno/badcputype.md)
  Bad CPU type in executable.
- [static var badExecutable: Errno](errno/badexecutable.md)
  Bad executable or shared library.
- [static var execFormatError: Errno](errno/execformaterror.md)
  Executable format error.
- [static var malformedMachO: Errno](errno/malformedmacho.md)
  Malformed Mach-O file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/sharedlibraryversionmismatch)*