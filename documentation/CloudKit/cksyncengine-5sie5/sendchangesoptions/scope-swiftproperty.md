# scope

**Framework**: CloudKit  
**Kind**: property

The scope of the changes to send.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
var scope: CKSyncEngine.SendChangesOptions.Scope { get set }
```

#### Discussion

When creating the next batch of changes to send to the server, consult this and only send changes within this scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchangesoptions/scope-swift.property)*