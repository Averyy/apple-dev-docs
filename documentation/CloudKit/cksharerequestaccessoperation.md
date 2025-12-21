# CKShareRequestAccessOperation

**Framework**: CloudKit  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class CKShareRequestAccessOperation
```

## Topics

### Initializers
- [init()](cksharerequestaccessoperation/init.md)
  Creates a new, empty share request access operation.
- [convenience init(shareURLs: [URL])](cksharerequestaccessoperation/init(shareurls:).md)
  Creates a share request access operation configured with specified share URLs.
### Instance Properties
- [var perShareAccessRequestResultBlock: ((URL, Result<Void, any Error>) -> Void)?](cksharerequestaccessoperation/pershareaccessrequestresultblock.md)
  A block called once for each share URL processed by the server.
- [var shareAccessRequestResultBlock: ((Result<Void, any Error>) -> Void)?](cksharerequestaccessoperation/shareaccessrequestresultblock.md)
  A block called when the entire share access request operation completes.
- [var shareURLs: [URL]?](cksharerequestaccessoperation/shareurls.md)
  The URLs of the shares to request access to.

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