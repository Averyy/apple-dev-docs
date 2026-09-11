# closeOnFork

**Framework**: System  
**Kind**: property

Indicates that forking a program closes the file.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var closeOnFork: FileDescriptor.DuplicateOptions { get }
```

#### Discussion

Normally, file descriptors remain open across calls to the `fork(2)` function. If you specify this option, the file descriptor is closed when forking this process into another process.

The state of the file descriptor flags can be inspected using `F_GETFD`, as described in the `fcntl(2)` man page.

The corresponding C constant is `O_CLOFORK`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/duplicateoptions/closeonfork)*