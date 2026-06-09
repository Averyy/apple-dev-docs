# invalidate()

**Framework**: Foundation  
**Kind**: method

Invalidates an activity and marks it as no longer eligible for continuation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

Call this method when the user stops engaging in the associated activity and that activity is no longer available. For example, you might call this method when the user closes the window associated with the activity. After calling this method on a user activity object, calling the [`becomeCurrent()`](nsuseractivity/becomecurrent().md) method on that object has no effect.

## See Also

- [func becomeCurrent()](nsuseractivity/becomecurrent.md)
  Marks the activity as currently in use by the user.
- [func resignCurrent()](nsuseractivity/resigncurrent.md)
  Marks this activity object as inactive without invalidating it.
- [var needsSave: Bool](nsuseractivity/needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](nsuseractivity/deleteallsaveduseractivities(completionhandler:).md)
  Deletes all user activities created by your app.
- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:).md)
  Deletes user activities created by your app that have the specified persistent identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/invalidate())*