# pipe()

**Framework**: System  
**Kind**: method

Creates a unidirectional data channel, which can be used for interprocess communication.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
static func pipe() throws -> (readEnd: FileDescriptor, writeEnd: FileDescriptor)
```

#### Return Value

The pair of file descriptors.

#### Discussion

The corresponding C function is `pipe`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/pipe())*