# typeIdentifier

**Framework**: File Provider  
**Kind**: property

The item’s Uniform Type Identifier (UTI).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var typeIdentifier: String { get }
```

#### Discussion

Your extension must provide either the [`typeIdentifier`](nsfileprovideritemprotocol/typeidentifier.md) or the [`contentType`](nsfileprovideritemprotocol/contenttype.md) property. Use the [`typeIdentifier`](nsfileprovideritemprotocol/typeidentifier.md) property only in iOS 13 or earlier.

## See Also

- [var itemIdentifier: NSFileProviderItemIdentifier](nsfileprovideritemprotocol/itemidentifier.md)
  The item’s persistent identifier.
- [var filename: String](nsfileprovideritemprotocol/filename.md)
  The item’s filename.
- [var contentType: UTType](nsfileprovideritemprotocol/contenttype.md)
  The item’s Uniform Type Identifier (UTI).
- [var capabilities: NSFileProviderItemCapabilities](nsfileprovideritemprotocol/capabilities.md)
  The item’s capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/typeidentifier)*