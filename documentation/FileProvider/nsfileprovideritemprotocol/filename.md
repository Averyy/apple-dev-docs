# filename

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The item’s filename.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var filename: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * filename;
```

## See Also

### Providing Required Properties
- [var itemIdentifier: NSFileProviderItemIdentifier](./itemidentifier.md)
  The item’s persistent identifier.
- [var typeIdentifier: String](./typeidentifier.md)
  The item’s Uniform Type Identifier (UTI).
- [var contentType: UTType](./contenttype.md)
  The item’s Uniform Type Identifier (UTI).
- [var capabilities: NSFileProviderItemCapabilities](./capabilities.md)
  The item’s capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/filename)*