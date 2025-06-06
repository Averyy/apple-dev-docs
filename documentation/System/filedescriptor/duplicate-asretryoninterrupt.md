# duplicate(as:retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Duplicates this file descriptor and return the newly created copy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func duplicate(as target: FileDescriptor? = nil, retryOnInterrupt: Bool = true) throws -> FileDescriptor
```

#### Return Value

The new file descriptor.

#### Discussion

If the `target` descriptor is already in use, then it is first deallocated as if a close(2) call had been done first.

File descriptors are merely references to some underlying system resource. The system does not distinguish between the original and the new file descriptor in any way. For example, read, write and seek operations on one of them also affect the logical file position in the other, and append mode, non-blocking I/O and asynchronous I/O options are shared between the references. If a separate pointer into the file is desired, a different object reference to the file must be obtained by issuing an additional call to `open`.

However, each file descriptor maintains its own close-on-exec flag.

The corresponding C functions are `dup` and `dup2`.

## Parameters

- `retryOnInterrupt`: Whether to retry the write operation   if it throws  . The default is  .   Pass   to try only once and throw an error upon interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/duplicate(as:retryoninterrupt:))*