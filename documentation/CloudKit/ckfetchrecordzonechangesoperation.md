# CKFetchRecordZoneChangesOperation

**Framework**: CloudKit  
**Kind**: class

An operation that fetches record zone changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKFetchRecordZoneChangesOperation
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)

#### Overview

Use this operation to fetch record changes in one or more record zones, such as those that occur during record creation, modification, and deletion. You provide a configuration object for each record zone to query for changes. The configuration contains a server change token, which is an opaque pointer to a specific change in the zone’s history. CloudKit returns only the changes that occur after that point. For the first time you fetch a record zone’s changes, or to refetch all changes in a zone’s history, use `nil` instead.

> **Note**:  Only private and shared databases support this operation. If you attempt to execute this operation in the public database, CloudKit returns an error.

CloudKit processes the record zones in succession, and returns the changes for each zone in batches. Each batch yields a new change token. If all batches return without error, the operation issues a final change token for that zone. The change tokens conform to [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) and are safe to cache on-disk. This operation’s tokens aren’t compatible with [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md) so you should segregate them in your app’s cache. Don’t infer behavior or order from the tokens’ contents.

If you create record zones in the private database, fetch all changes the first time the app launches. Cache the results on-device and use [`CKRecordZoneSubscription`](ckrecordzonesubscription.md) to subscribe to future changes. Fetch those changes on receipt of the push notifications the subscription generates. If you use the shared database, subscribe to changes with [`CKDatabaseSubscription`](ckdatabasesubscription.md) instead. When a user participates in sharing, CloudKit adds and removes record zones. This means you don’t know in advance which zones exist in the shared database. Use [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md) to fetch shared record zones on receipt of the subscription’s push notifications. Then fetch the changes in those zones using this operation. Regardless of which database you use, it’s not necessary to perform fetches each time your app launches, or to schedule fetches at regular intervals.

To run the operation, add it to the corresponding database’s operation queue. The operation executes its callbacks on a private serial queue.

The following example demonstrates how to create the operation, configure its callbacks, and execute it. For brevity, it omits the delete and operation completion callbacks.

```swift
// Create a dictionary that maps a record zone ID to its
// corresponding zone configuration. The configuration
// contains the server change token from the most recent 
// fetch of that record zone.
NSMutableDictionary *configurations = [NSMutableDictionary new];
for (CKRecordZoneID *recordZoneID in recordZoneIDs) {
    CKFetchRecordZoneChangesConfiguration *config = 
        [CKFetchRecordZoneChangesConfiguration new];
    config.previousServerChangeToken = [tokenCache objectForKey:recordZoneID];
    [configurations setObject:config forKey:recordZoneID];
}

// Create a fetch operation with an array of record zone IDs
// and the zone configuration mapping dictionary. 
CKFetchRecordZoneChangesOperation *operation = 
    [[CKFetchRecordZoneChangesOperation alloc] 
     initWithRecordZoneIDs:recordZoneIDs 
     configurationsByRecordZoneID:configurations];

// Process each changed record as CloudKit returns it.   
operation.recordChangedBlock = ^(CKRecord *record) {
    recordHandler(record);
};

// Cache the change tokens that CloudKit provides as
// the operation runs.
operation.recordZoneChangeTokensUpdatedBlock = ^(CKRecordZoneID *recordZoneID, 
                                                 CKServerChangeToken *token, 
                                                 NSData *data) {
    [tokenCache setObject:token forKey:recordZoneID];
};

// If the fetch for the current record zone completes
// successfully, cache the final change token.    
operation.recordZoneFetchCompletionBlock = ^(CKRecordZoneID *recordZoneID, 
                                             CKServerChangeToken *token, 
                                             NSData *data, BOOL more, 
                                             NSError *error) {
    if (error) {
        // Handle the error.
    } else {
        [tokenCache setObject:token forKey:recordZoneID];
    }
};

// Set an appropriate QoS and add the operation to the shared
// database's operation queue to execute it.
operation.qualityOfService = NSQualityOfServiceUtility;
[CKContainer.defaultContainer.sharedCloudDatabase addOperation:operation];
```

## Topics

### Creating a Zone Change Operation
- [convenience init(recordZoneIDs: [CKRecordZone.ID]?, configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]?)](ckfetchrecordzonechangesoperation/init(recordzoneids:configurationsbyrecordzoneid:).md)
  Creates an operation for fetching record zone changes.
- [init()](ckfetchrecordzonechangesoperation/init.md)
  Creates an empty fetch record zone changes operation.
### Configuring the Zone Change Operation
- [var configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]?](ckfetchrecordzonechangesoperation/configurationsbyrecordzoneid.md)
  A dictionary of configurations for fetching change operations by zone identifier.
- [CKFetchRecordZoneChangesOperation.ZoneConfiguration](ckfetchrecordzonechangesoperation/zoneconfiguration.md)
  A configuration object that describes the information to fetch from a record zone.
- [var fetchAllChanges: Bool](ckfetchrecordzonechangesoperation/fetchallchanges.md)
  A Boolean value that indicates whether to send repeated requests to the server.
- [var recordZoneIDs: [CKRecordZone.ID]?](ckfetchrecordzonechangesoperation/recordzoneids.md)
  The IDs of the record zones that contain the records to fetch.
### Processing the Zone Change Operation Results
- [var recordChangedBlock: ((CKRecord) -> Void)?](ckfetchrecordzonechangesoperation/recordchangedblock.md)
  The closure to execute with the contents of a changed record.
- [var recordWithIDWasDeletedBlock: ((CKRecord.ID, CKRecord.RecordType) -> Void)?](ckfetchrecordzonechangesoperation/recordwithidwasdeletedblock-3z14c.md)
  The closure to execute when a record no longer exists.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonefetchcompletionblock.md)
  The closure to execute when a record zone’s fetch finishes.
- [var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/fetchrecordzonechangescompletionblock.md)
  The closure to execute when the operation finishes.
### Deprecated
- [Deprecated Symbols](ckfetchrecordzonechangesoperation-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var fetchRecordZoneChangesResultBlock: ((Result<Void, any Error>) -> Void)?](ckfetchrecordzonechangesoperation/fetchrecordzonechangesresultblock.md)
- [var recordWasChangedBlock: ((CKRecord.ID, Result<CKRecord, any Error>) -> Void)?](ckfetchrecordzonechangesoperation/recordwaschangedblock-x5bw.md)
- [var recordZoneFetchResultBlock: ((CKRecordZone.ID, Result<(serverChangeToken: CKServerChangeToken, clientChangeTokenData: Data?, moreComing: Bool), any Error>) -> Void)?](ckfetchrecordzonechangesoperation/recordzonefetchresultblock.md)

## Relationships

### Inherits From
- [CKDatabaseOperation](ckdatabaseoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKRecordZoneSubscription](ckrecordzonesubscription.md)
  A subscription that generates push notifications when CloudKit modifies records in a specific record zone.
- [class CKRecordZoneNotification](ckrecordzonenotification.md)
  A notification that triggers when the contents of a record zone change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation)*