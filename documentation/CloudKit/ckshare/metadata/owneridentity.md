# ownerIdentity

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The identity of the share’s owner.

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
@NSCopying
var ownerIdentity: CKUserIdentity { get }
```

```objc
@property (copy, readonly) CKUserIdentity * ownerIdentity;
```

## See Also

### Accessing the Share
- [var share: CKShare](./share.md)
  The share that owns the metadata.
- [var containerIdentifier: String](./containeridentifier.md)
  The ID of the share’s container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/owneridentity)*