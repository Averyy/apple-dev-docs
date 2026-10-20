# group

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The operation’s group.

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
var group: CKOperationGroup? { get set }
```

```objc
@property (nonatomic, strong, nullable) CKOperationGroup * group;
```

## See Also

### Managing the Operation’s Configuration
- [var configuration: CKOperation.Configuration!](./configuration-swift.property.md)
  The operation’s configuration.
- [CKOperation.Configuration](./configuration-swift.class.md)
  An object that describes how a CloudKit operation behaves.
- [var longLivedOperationWasPersistedBlock: (() -> Void)?](./longlivedoperationwaspersistedblock.md)
  The closure to execute when the server begins to store callbacks for the long-lived operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/group)*