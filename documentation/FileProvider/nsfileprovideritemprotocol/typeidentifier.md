# typeIdentifier

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

The item’s Uniform Type Identifier (UTI).

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`contentType`](./contenttype.md) instead.

## Declaration

```swift
optional var typeIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * typeIdentifier;
```

## Discussion

Your extension must provide either the [`typeIdentifier`](./typeidentifier.md) or the [`contentType`](./contenttype.md) property. Use the [`typeIdentifier`](./typeidentifier.md) property only in iOS 13 or earlier.

## See Also

### Providing Required Properties
- [var itemIdentifier: NSFileProviderItemIdentifier](./itemidentifier.md)
  The item’s persistent identifier.
- [var filename: String](./filename.md)
  The item’s filename.
- [var contentType: UTType](./contenttype.md)
  The item’s Uniform Type Identifier (UTI).
- [var capabilities: NSFileProviderItemCapabilities](./capabilities.md)
  The item’s capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/typeidentifier)*