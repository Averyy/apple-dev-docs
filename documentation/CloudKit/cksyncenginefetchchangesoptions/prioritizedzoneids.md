# prioritizedZoneIDs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A list of zones that are prioritized over others while fetching changes.

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
@property (copy) NSArray<CKRecordZoneID *> * prioritizedZoneIDs;
```

#### Discussion

`CKSyncEngine` fetches changes for the zones in this list first. You might use this to prioritize a specific set of zones for initial sync. You could also prioritize the object currently showing in the UI by putting it first in this list.

Any zones not included in this list are prioritized in a default manner. If a zone in this list has no changes to fetch, then that zone is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefetchchangesoptions/prioritizedzoneids)*