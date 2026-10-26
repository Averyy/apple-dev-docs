# initWithZoneIDs:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a scope that contains only the given zone IDs. If `zoneIDs` is `nil`, then this scope contains all zones.

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
- (instancetype) initWithZoneIDs:(NSSet<CKRecordZoneID *> *) zoneIDs;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesendchangesscope/initwithzoneids:)*