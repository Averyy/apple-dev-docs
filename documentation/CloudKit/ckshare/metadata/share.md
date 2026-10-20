# share

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The share that owns the metadata.

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
var share: CKShare { get }
```

```objc
@property (copy, readonly) CKShare * share;
```

## See Also

### Accessing the Share
- [var containerIdentifier: String](./containeridentifier.md)
  The ID of the share’s container.
- [var ownerIdentity: CKUserIdentity](./owneridentity.md)
  The identity of the share’s owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/share)*