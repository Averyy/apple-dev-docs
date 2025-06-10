# CKShareRequestAccessOperation

**Framework**: CloudKit  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class CKShareRequestAccessOperation
```

## Topics

### Initializers
- [init()](cksharerequestaccessoperation/init.md)
- [convenience init(shareURLs: [URL])](cksharerequestaccessoperation/init(shareurls:).md)
  Creates a [`CKShareRequestAccessOperation`](cksharerequestaccessoperation.md) for requesting access to the specified shares.
### Instance Properties
- [var perShareAccessRequestResultBlock: ((URL, Result<Void, any Error>) -> Void)?](cksharerequestaccessoperation/pershareaccessrequestresultblock.md)
  Called once for each share URL that the server processed
- [var shareAccessRequestResultBlock: ((Result<Void, any Error>) -> Void)?](cksharerequestaccessoperation/shareaccessrequestresultblock.md)
  This block is called when the operation completes.
- [var shareURLs: [URL]?](cksharerequestaccessoperation/shareurls.md)
  The share URLs for which access is being requested.

## Relationships

### Inherits From
- [CKOperation](ckoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation)*