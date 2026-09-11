# pipe(options:)

**Framework**: System  
**Kind**: method

Creates a unidirectional data channel, which can be used for interprocess communication.

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