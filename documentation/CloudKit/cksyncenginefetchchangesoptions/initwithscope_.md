# initWithScope:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Initializes a set of options with the specific scope.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (instancetype) initWithScope:(CKSyncEngineFetchChangesScope *) scope;
```

#### Discussion

If you provide a `nil` scope, the default scope is used. The default scope includes everything.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefetchchangesoptions/initwithscope:)*