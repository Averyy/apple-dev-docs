# syncEngine:nextFetchChangesOptionsForContext:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Returns a custom set of options for CKSyncEngine to use while fetching changes.

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
- (CKSyncEngineFetchChangesOptions *) syncEngine:(CKSyncEngine *) syncEngine nextFetchChangesOptionsForContext:(CKSyncEngineFetchChangesContext *) context;
```

#### Discussion

While `CKSyncEngine` fetches changes from the server, it calls this function to determine priority and other options for fetching changes.

For example, you can use this to prioritize fetching the object currently showing in the UI. You can also use this to prioritize specific zones during initial sync.

By default, `CKSyncEngine` uses whatever options are in the context. You can return `context.options` if you don’t want to perform any customization.

This callback is called in between each server request while fetching changes. This allows the fetching mechanism to react dynamically while your app state changes.

An example implementation might look something like this:

```objc
- (CKSyncEngineFetchChangesOptions *)syncEngine:(CKSyncEngine *)syncEngine nextFetchChangesOptionsForContext:(CKSyncEngineFetchChangesContext *)context {

    // Start with the options from the context.
    CKSyncEngineFetchChangesOptions *options = context.options;

    // By default, the sync engine will automatically fetch changes for all zones.
    // If you know that you only want to sync a specific set of zones, you can override that here.
    options.scope = [[CKSyncEngineFetchChangesScope alloc] initWithZoneIDs:@[...]];

    // You can prioritize specific zones to be fetched first by putting them in order.
    NSMutableArray<CKRecordZoneID *> *prioritizedZoneIDs = [[NSMutableArray alloc] init];

    // If you're showing some data in the UI, you might want to prioritize that zone first.
    CKRecordZoneID *onScreenZoneID = uiController.currentlyViewedItem.zoneID;
    if (onScreenZoneID != nil) {
        [prioritizedZoneIDs addObject:onScreenZoneID];
    }

    // You could also prioritize special, well-known zones if that makes sense for your app.
    // For example, if you have a top-level metadata zone that you'd like to sync first, you can prioritize that here.
    CKRecordZoneID *topLevelZoneID = [[CKRecordZoneID alloc] initWithZoneName:@"MyImportantMetadata"];
    [prioritizedZoneIDs addObject:topLevelZoneID];

    options.prioritizedZoneIDs = prioritizedZoneIDs;
    return options;
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedelegate-3c38p/syncengine:nextfetchchangesoptionsforcontext:)*