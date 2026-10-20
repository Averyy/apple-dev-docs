# NSPersistentHistoryTrackingKey

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

The key you use to enable persistent history tracking.

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
let NSPersistentHistoryTrackingKey: String
```

```c
extern NSString * const NSPersistentHistoryTrackingKey;
```

## Mentions

- [Consuming relevant store changes](./consuming-relevant-store-changes.md)

#### Discussion

Persistent history tracking is off by default.

## See Also

### Maintaining a record of changes
- [func currentPersistentHistoryToken(fromStores: [Any]?) -> NSPersistentHistoryToken?](./nspersistentstorecoordinator/currentpersistenthistorytoken%28fromstores%29.md)
  Returns a single persistent history token representing all of the specified stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorytrackingkey)*