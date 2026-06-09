# nonBlocking

**Framework**: System  
**Kind**: property

Indicates that all subsequent input and output operations on the pipe’s file descriptors will be nonblocking.

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
static var nonBlocking: FileDescriptor.PipeOptions { get }
```

#### Discussion

The corresponding C constant is `O_NONBLOCK`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/pipeoptions/nonblocking)*