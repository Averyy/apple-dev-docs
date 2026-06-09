# closeOnFork

**Framework**: System  
**Kind**: property

Indicates that forking a program closes the file.

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
static var closeOnFork: FileDescriptor.DuplicateOptions { get }
```

#### Discussion

Normally, file descriptors remain open across calls to the `fork(2)` function. If you specify this option, the file descriptor is closed when forking this process into another process.

The state of the file descriptor flags can be inspected using `F_GETFD`, as described in the `fcntl(2)` man page.

The corresponding C constant is `O_CLOFORK`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/duplicateoptions/closeonfork)*