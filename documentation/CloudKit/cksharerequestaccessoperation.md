# CKShareRequestAccessOperation

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface CKShareRequestAccessOperation : CKOperation
```

## Topics

### Initializers
- [init()](./cksharerequestaccessoperation/init%28%29.md)
  Creates a new, empty share request access operation.
- [convenience init(shareURLs: [URL])](./cksharerequestaccessoperation/init%28shareurls%29.md)
  Creates a share request access operation configured with specified share URLs.
### Instance Properties
- [var perShareAccessRequestResultBlock: ((URL, Result<Void, any Error>) -> Void)?](./cksharerequestaccessoperation/pershareaccessrequestresultblock.md)
  The closure to execute when CloudKit processes a share access request.
- [var shareAccessRequestResultBlock: ((Result<Void, any Error>) -> Void)?](./cksharerequestaccessoperation/shareaccessrequestresultblock.md)
  The closure to execute after CloudKit processes each share access request.
- [var shareURLs: [URL]?](./cksharerequestaccessoperation/shareurls.md)
  The URLs of the shares to request access to.
- [perShareAccessRequestCompletionBlock](./cksharerequestaccessoperation/pershareaccessrequestcompletionblock.md)
  The closure to execute when CloudKit processes a share access request.
- [shareRequestAccessCompletionBlock](./cksharerequestaccessoperation/sharerequestaccesscompletionblock.md)
  The closure to execute after CloudKit processes all share access requests.

## Relationships

### Inherits From
- [CKOperation](./ckoperation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation)*