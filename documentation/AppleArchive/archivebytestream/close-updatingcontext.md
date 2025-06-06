# close(updatingContext:)

**Framework**: Apple Archive  
**Kind**: method

Closes the stream, releases associated resources, and writes the sealed container attributes to the specified encryption context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func close(updatingContext context: ArchiveEncryptionContext) throws
```

## Parameters

- `context`: The encryption context that receives the sealed container attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/close(updatingcontext:))*