# pipe(options:)

**Framework**: System  
**Kind**: method

Creates a unidirectional data channel, which can be used for interprocess communication.

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
static func pipe(options: FileDescriptor.PipeOptions) throws(Errno) -> (readEnd: FileDescriptor, writeEnd: FileDescriptor)
```

#### Return Value

The pair of file descriptors.

#### Discussion

The corresponding C function is `pipe2`.

## Parameters

- `options`: The behavior for creating the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/pipe(options:))*