# deleteAllSavedUserActivities(completionHandler:)

**Framework**: Foundation  
**Kind**: method

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
class func deleteAllSavedUserActivities() async
```

#### Discussion

Deletes all user activities stored by Core Spotlight or donated as Siri shortcuts.

## Parameters

- `handler`: The block that the system invokes after deleting the user activities. Wait for the system to call this block to ensure that the system deletes the activities (or marks them for deletion).

## See Also

- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:).md)
  Deletes user activities created by your app that have the specified persistent identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/deleteallsaveduseractivities(completionhandler:))*