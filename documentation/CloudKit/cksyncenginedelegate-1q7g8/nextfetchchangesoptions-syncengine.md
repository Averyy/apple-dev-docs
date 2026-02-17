# nextFetchChangesOptions(_:syncEngine:)

**Framework**: CloudKit  
**Kind**: method  
**Required**: Yes

Returns a custom set of options for [`CKSyncEngine`](cksyncengine-5sie5.md) to use while fetching changes.

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
func nextFetchChangesOptions(_ context: CKSyncEngine.FetchChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.FetchChangesOptions
```

#### Return Value

Customized fetch options for the current fetch operation, or `context.options` to use the default options without customization.

#### Discussion

While [`CKSyncEngine`](cksyncengine-5sie5.md) fetches changes from the server, it calls this function to determine priority and other options for fetching changes.

For example, you can use this to prioritize fetching the object currently showing in the UI. You can also use this to prioritize specific zones during initial sync.

By default, [`CKSyncEngine`](cksyncengine-5sie5.md) uses whatever options are in the context. You can return `context.options` if you don’t want to perform any customization.

This callback is called in between each server request while fetching changes. This allows the fetching mechanism to react dynamically while your app state changes.

An example implementation might look something like this:

```swift
func nextFetchChangesOptions(_ context: CKSyncEngine.FetchChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.FetchChangesOptions {

    // Start with the options from the context.
    var options = context.options

    // By default, the sync engine automatically fetches changes for all zones.
    // If you know that you only want to sync a specific set of zones, you can override that here.
    options.scope = .zoneIDs([...])

    // You can prioritize specific zones to be fetched first by putting them in order.
    var prioritizedZoneIDs: [CKRecordZone.ID] = []

    // If you're showing some data in the UI, you might want to prioritize that zone first.
    if let onScreenZoneID = uiController.currentlyViewedItem.zoneID {
        prioritizedZoneIDs.append(onScreenZoneID)
    }

    // You could also prioritize special, well-known zones if that makes sense for your app.
    // For example, if you have a top-level metadata zone that you'd like to sync first, you can prioritize that here.
    let topLevelZoneID = CKRecordZone.ID(zoneName: "MyImportantMetadata")
    prioritizedZoneIDs.append(topLevelZoneID)

    options.prioritizedZoneIDs = prioritizedZoneIDs
    return options
}
```

## Parameters

- `context`: The context of the fetch operation, including the current options and reason for fetching.
- `syncEngine`: The sync engine requesting the options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedelegate-1q7g8/nextfetchchangesoptions(_:syncengine:))*