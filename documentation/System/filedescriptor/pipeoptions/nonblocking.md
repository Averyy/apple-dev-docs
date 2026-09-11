# nonBlocking

**Framework**: System  
**Kind**: property

Indicates that all subsequent input and output operations on the pipe’s file descriptors will be nonblocking.

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
static var nonBlocking: FileDescriptor.PipeOptions { get }
```

#### Discussion

The corresponding C constant is `O_NONBLOCK`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/pipeoptions/nonblocking)*