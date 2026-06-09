# duplicate(as:options:retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Duplicates this file descriptor and returns the newly created copy.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func duplicate(as target: FileDescriptor, options: FileDescriptor.DuplicateOptions, retryOnInterrupt: Bool = true) throws(Errno) -> FileDescriptor
```

#### Return Value

The new file descriptor.

#### Discussion

If the `target` descriptor is already in use, then it is first deallocated as if a close(2) call had been done first.

File descriptors are merely references to some underlying system resource. The system does not distinguish between the original and the new file descriptor in any way. For example, read, write and seek operations on one of them also affect the logical file position in the other, and append mode, non-blocking I/O and asynchronous I/O options are shared between the references. If a separate pointer into the file is desired, a different object reference to the file must be obtained by issuing an additional call to `open`.

However, each file descriptor maintains its own close-on-exec flag.

The corresponding C function is `dup3`.

## Parameters

- `retryOnInterrupt`: Whether to retry the duplicate operation if it throws [`interrupted`](errno/interrupted.md). The default is `true`. Pass `false` to try only once and throw an error upon interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/duplicate(as:options:retryoninterrupt:))*