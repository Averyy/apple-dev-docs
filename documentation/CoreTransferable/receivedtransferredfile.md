# ReceivedTransferredFile

**Framework**: Core Transferable  
**Kind**: struct

A description of a file from the perspective of the receiver.

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
struct ReceivedTransferredFile
```

## Topics

### Configuring a file transfer
- [let file: URL](receivedtransferredfile/file.md)
  The received file on disk.
- [let isOriginalFile: Bool](receivedtransferredfile/isoriginalfile.md)
  A Boolean value that indicates whether the file’s URL points to the original file provided by the sender or to a copy.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FileRepresentation](filerepresentation.md)
  A transfer representation for types that transfer as a file URL.
- [struct SentTransferredFile](senttransferredfile.md)
  A description of a file from the perspective of the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/receivedtransferredfile)*