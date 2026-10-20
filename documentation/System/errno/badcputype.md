# badCPUType

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Bad CPU type in executable.

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
static var badCPUType: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

The specified executable doesn’t support the current CPU.

The corresponding C error is `EBADARCH`.

## See Also

### Executable File Errors
- [static var badExecutable: Errno](./badexecutable.md)
  Bad executable or shared library.
- [static var execFormatError: Errno](./execformaterror.md)
  Executable format error.
- [static var malformedMachO: Errno](./malformedmacho.md)
  Malformed Mach-O file.
- [static var sharedLibraryVersionMismatch: Errno](./sharedlibraryversionmismatch.md)
  Shared library version mismatch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/badcputype)*