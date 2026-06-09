# closeOnExec

**Framework**: System  
**Kind**: property

Indicates that executing a program closes the file.

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
static var closeOnExec: FileDescriptor.DuplicateOptions { get }
```

#### Discussion

Normally, file descriptors remain open across calls to the `exec(2)` family of functions. If you specify this option, the file descriptor is closed when replacing this process with another process.

The state of the file descriptor flags can be inspected using `F_GETFD`, as described in the `fcntl(2)` man page.

The corresponding C constant is `O_CLOEXEC`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/duplicateoptions/closeonexec)*