# deleteSavedUserActivities(withPersistentIdentifiers:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Deletes user activities created by your app that have the specified persistent identifiers.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func deleteSavedUserActivities(withPersistentIdentifiers persistentIdentifiers: [NSUserActivityPersistentIdentifier]) async
```

#### Discussion

Deletes user activities with a persistent identifier matching any identifier in the `persistentIdentifiers` array.

## Parameters

- `persistentIdentifiers`: The list of persistent identifiers that the system uses to determine which user activities to delete.
- `handler`: The block that the system invokes after deleting the user activities. Wait for the system to call this block to ensure that the system deletes the activities (or marks them for deletion).

## See Also

- [func becomeCurrent()](nsuseractivity/becomecurrent.md)
  Marks the activity as currently in use by the user.
- [func resignCurrent()](nsuseractivity/resigncurrent.md)
  Marks this activity object as inactive without invalidating it.
- [func invalidate()](nsuseractivity/invalidate.md)
  Invalidates an activity and marks it as no longer eligible for continuation.
- [var needsSave: Bool](nsuseractivity/needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](nsuseractivity/deleteallsaveduseractivities(completionhandler:).md)
  Deletes all user activities created by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:))*