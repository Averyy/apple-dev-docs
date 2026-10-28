# deleteAllSavedUserActivities(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Deletes all user activities created by your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func deleteAllSavedUserActivities(completionHandler handler: @escaping @Sendable () -> Void)
```

```swift
class func deleteAllSavedUserActivities() async
```

```objc
+ (void) deleteAllSavedUserActivitiesWithCompletionHandler:(void (^)()) handler;
```

## Discussion

Deletes all user activities stored by Core Spotlight or donated as Siri shortcuts.

## Parameters

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
- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](./deletesaveduseractivities%28withpersistentidentifiers,completionhandler%29.md)
  Deletes user activities created by your app that have the specified persistent identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/deleteallsaveduseractivities(completionhandler:))*