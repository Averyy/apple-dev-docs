# configuration

**Framework**: CloudKit  
**Kind**: property

The operation’s configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var configuration: CKOperation.Configuration! { get set }
```

## See Also

- [CKOperation.Configuration](ckoperation/configuration-swift.class.md)
  An object that describes how a CloudKit operation behaves.
- [var group: CKOperationGroup?](ckoperation/group.md)
  The operation’s group.
- [var longLivedOperationWasPersistedBlock: (() -> Void)?](ckoperation/longlivedoperationwaspersistedblock.md)
  The closure to execute when the server begins to store callbacks for the long-lived operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/configuration-swift.property)*