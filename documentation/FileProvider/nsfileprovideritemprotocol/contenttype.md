# contentType

**Framework**: File Provider  
**Kind**: property

The item’s Uniform Type Identifier (UTI).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
optional var contentType: UTType { get }
```

#### Discussion

Your extension must provide either the [`typeIdentifier`](nsfileprovideritemprotocol/typeidentifier.md) or the [`contentType`](nsfileprovideritemprotocol/contenttype.md) property. Where possible, use the [`contentType`](nsfileprovideritemprotocol/contenttype.md) property. Use the [`typeIdentifier`](nsfileprovideritemprotocol/typeidentifier.md) property only in iOS 13 or earlier.

## See Also

- [var itemIdentifier: NSFileProviderItemIdentifier](nsfileprovideritemprotocol/itemidentifier.md)
  The item’s persistent identifier.
- [var filename: String](nsfileprovideritemprotocol/filename.md)
  The item’s filename.
- [var typeIdentifier: String](nsfileprovideritemprotocol/typeidentifier.md)
  The item’s Uniform Type Identifier (UTI).
- [var capabilities: NSFileProviderItemCapabilities](nsfileprovideritemprotocol/capabilities.md)
  The item’s capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/contenttype)*