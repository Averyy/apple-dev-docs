# deleteSavedUserActivities(withPersistentIdentifiers:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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
class func deleteSavedUserActivities(withPersistentIdentifiers persistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler handler: @escaping @Sendable () -> Void)
```

```swift
class func deleteSavedUserActivities(withPersistentIdentifiers persistentIdentifiers: [NSUserActivityPersistentIdentifier]) async
```

```objc
+ (void) deleteSavedUserActivitiesWithPersistentIdentifiers:(NSArray<NSString *> *) persistentIdentifiers completionHandler:(void (^)()) handler;
```

#### Discussion

Deletes user activities with a persistent identifier matching any identifier in the `persistentIdentifiers` array.

## Parameters

- `persistentIdentifiers`: The list of persistent identifiers that the system uses to determine which user activities to delete.
- `handler`: The block that the system invokes after deleting the user activities. Wait for the system to call this block to ensure that the system deletes the activities (or marks them for deletion).

## See Also

### Registering and invalidating activities
- [func becomeCurrent()](./becomecurrent%28%29.md)
  Marks the activity as currently in use by the user.
- [func resignCurrent()](./resigncurrent%28%29.md)
  Marks this activity object as inactive without invalidating it.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates an activity and marks it as no longer eligible for continuation.
- [var needsSave: Bool](./needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](./deleteallsaveduseractivities%28completionhandler%29.md)
  Deletes all user activities created by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:))*