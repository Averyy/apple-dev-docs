# resignCurrent()

**Framework**: Foundation  
**Kind**: method

Marks this activity object as inactive without invalidating it.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func resignCurrent()
```

## Mentions

- [Supporting the creation of Quick Notes](supporting-the-creation-of-quick-notes.md)

#### Discussion

Calling this method marks the user activity as no longer current, but doesn’t invalidate it entirely. You can call this method when you want to stop advertising the activity for continuation and search indexing only temporarily. You may call [`becomeCurrent()`](nsuseractivity/becomecurrent().md) later to restore this object as the current activity.

## See Also

- [func becomeCurrent()](nsuseractivity/becomecurrent.md)
  Marks the activity as currently in use by the user.
- [func invalidate()](nsuseractivity/invalidate.md)
  Invalidates an activity and marks it as no longer eligible for continuation.
- [var needsSave: Bool](nsuseractivity/needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](nsuseractivity/deleteallsaveduseractivities(completionhandler:).md)
  Deletes all user activities created by your app.
- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:).md)
  Deletes user activities created by your app that have the specified persistent identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/resigncurrent())*