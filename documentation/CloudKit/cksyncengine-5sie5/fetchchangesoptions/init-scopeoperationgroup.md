# init(scope:operationGroup:)

**Framework**: CloudKit  
**Kind**: init

Creates a new set of fetch changes options.

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
init(scope: CKSyncEngine.FetchChangesOptions.Scope = .all, operationGroup: CKOperationGroup? = nil)
```

## Parameters

- `scope`: The scope in which to fetch changes. Defaults to  .
- `operationGroup`: The operation group to use for the underlying CloudKit operations. If  , a default operation group will be created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchangesoptions/init(scope:operationgroup:))*