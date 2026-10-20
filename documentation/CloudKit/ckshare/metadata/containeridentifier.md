# containerIdentifier

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The ID of the share’s container.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var containerIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * containerIdentifier;
```

## See Also

### Accessing the Share
- [var share: CKShare](./share.md)
  The share that owns the metadata.
- [var ownerIdentity: CKUserIdentity](./owneridentity.md)
  The identity of the share’s owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/containeridentifier)*