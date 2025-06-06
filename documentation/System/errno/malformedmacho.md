# malformedMachO

**Framework**: System  
**Kind**: property

Malformed Mach-O file.

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
static var malformedMachO: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The Mach object file is malformed.

The corresponding C error is `EBADMACHO`.

## See Also

- [static var badCPUType: Errno](errno/badcputype.md)
  Bad CPU type in executable.
- [static var badExecutable: Errno](errno/badexecutable.md)
  Bad executable or shared library.
- [static var execFormatError: Errno](errno/execformaterror.md)
  Executable format error.
- [static var sharedLibraryVersionMismatch: Errno](errno/sharedlibraryversionmismatch.md)
  Shared library version mismatch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/malformedmacho)*