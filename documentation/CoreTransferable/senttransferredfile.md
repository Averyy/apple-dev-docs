# SentTransferredFile

**Framework**: Core Transferable  
**Kind**: struct

A description of a file from the perspective of the sender.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct SentTransferredFile
```

## Topics

### Configuring a file transfer
- [init(URL, allowAccessingOriginalFile: Bool)](senttransferredfile/init(_:allowaccessingoriginalfile:).md)
  Creates a description of a file from the perspective of the sender.
- [let file: URL](senttransferredfile/file.md)
  A URL that describes the location of the file.
- [let allowAccessingOriginalFile: Bool](senttransferredfile/allowaccessingoriginalfile.md)
  A Boolean value that indicates whether the receiver can read and write the original file. When set to `false`, the receiver can only gain access to a copy of the file.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FileRepresentation](filerepresentation.md)
  A transfer representation for types that transfer as a file URL.
- [struct ReceivedTransferredFile](receivedtransferredfile.md)
  A description of a file from the perspective of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/senttransferredfile)*