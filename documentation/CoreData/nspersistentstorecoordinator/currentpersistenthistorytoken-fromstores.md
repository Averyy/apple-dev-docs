# currentPersistentHistoryToken(fromStores:)

**Framework**: Core Data  
**Kind**: method

Returns a single persistent history token representing all of the specified stores.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func currentPersistentHistoryToken(fromStores stores: [Any]?) -> NSPersistentHistoryToken?
```

#### Return Value

A persistent history token, or `nil` if the coordinator can’t create one.

#### Discussion

If you specify `nil` or provide an empty array, the coordinator attempts to create a token for all of its registered stores.

## Parameters

- `stores`: The persistent stores of interest.

## See Also

- [let NSPersistentHistoryTrackingKey: String](nspersistenthistorytrackingkey.md)
  The key you use to enable persistent history tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/currentpersistenthistorytoken(fromstores:))*