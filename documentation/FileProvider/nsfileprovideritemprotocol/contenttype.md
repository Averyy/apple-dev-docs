# contentType

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

The item’s Uniform Type Identifier (UTI).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
optional var contentType: UTType { get }
```

```objc
@property (nonatomic, copy, readonly) UTType * contentType;
```

## Discussion

Your extension must provide either the [`typeIdentifier`](./typeidentifier.md) or the [`contentType`](./contenttype.md) property. Where possible, use the [`contentType`](./contenttype.md) property. Use the [`typeIdentifier`](./typeidentifier.md) property only in iOS 13 or earlier.

## See Also

### Providing Required Properties
- [var itemIdentifier: NSFileProviderItemIdentifier](./itemidentifier.md)
  The item’s persistent identifier.
- [var filename: String](./filename.md)
  The item’s filename.
- [var typeIdentifier: String](./typeidentifier.md)
  The item’s Uniform Type Identifier (UTI).
- [var capabilities: NSFileProviderItemCapabilities](./capabilities.md)
  The item’s capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/contenttype)*