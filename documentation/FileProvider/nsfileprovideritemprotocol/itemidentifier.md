# itemIdentifier

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The item’s persistent identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var itemIdentifier: NSFileProviderItemIdentifier { get }
```

```objc
@property (nonatomic, copy, readonly) NSFileProviderItemIdentifier itemIdentifier;
```

## Mentions

- [Synchronizing the File Provider Extension](../synchronizing-the-file-provider-extension.md)
- [Using push notifications to signal changes](../using-push-notifications-to-signal-changes.md)

## See Also

### Providing Required Properties
- [var filename: String](./filename.md)
  The item’s filename.
- [var typeIdentifier: String](./typeidentifier.md)
  The item’s Uniform Type Identifier (UTI).
- [var contentType: UTType](./contenttype.md)
  The item’s Uniform Type Identifier (UTI).
- [var capabilities: NSFileProviderItemCapabilities](./capabilities.md)
  The item’s capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/itemidentifier)*