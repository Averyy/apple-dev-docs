# zoneIDsWithUnfetchedServerChanges

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The identifiers of zones with changes on the server that have not yet been fetched.

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
@property (copy, readonly) NSArray<CKRecordZoneID *> * zoneIDsWithUnfetchedServerChanges;
```

## Discussion

The sync engine populates this list automatically, for example when receiving a push notification indicating new changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginestate/zoneidswithunfetchedserverchanges)*