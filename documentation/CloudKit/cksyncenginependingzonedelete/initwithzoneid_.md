# initWithZoneID:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a pending zone delete for the specified record zone identifier.

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
- (instancetype) initWithZoneID:(CKRecordZoneID *) zoneID;
```

#### Return Value

An initialized pending zone delete.

## Parameters

- `zoneID`: The unique identifier of the record zone to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginependingzonedelete/initwithzoneid:)*