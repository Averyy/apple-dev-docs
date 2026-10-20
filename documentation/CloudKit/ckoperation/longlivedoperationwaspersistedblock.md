# longLivedOperationWasPersistedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when the server begins to store callbacks for the long-lived operation.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var longLivedOperationWasPersistedBlock: (() -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^longLivedOperationWasPersistedBlock)();
```

#### Discussion

If your app exits before CloudKit calls this property’s value, the system doesn’t include the operation’s ID in the results of calls to the [`allLongLivedOperationIDs()`](../ckcontainer/alllonglivedoperationids%28%29.md) method.

For more information, see [Long-Lived Operations](../ckoperation.md#Long-Lived-Operations).

## See Also

### Managing the Operation’s Configuration
- [var configuration: CKOperation.Configuration!](./configuration-swift.property.md)
  The operation’s configuration.
- [CKOperation.Configuration](./configuration-swift.class.md)
  An object that describes how a CloudKit operation behaves.
- [var group: CKOperationGroup?](./group.md)
  The operation’s group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/longlivedoperationwaspersistedblock)*