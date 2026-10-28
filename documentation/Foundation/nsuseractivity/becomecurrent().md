# becomeCurrent()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Marks the activity as currently in use by the user.

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
func becomeCurrent()
```

```objc
- (void) becomeCurrent;
```

## Mentions

- [Creating a user activity object](../creating-a-user-activity-object.md)
- [Supporting the creation of Quick Notes](../supporting-the-creation-of-quick-notes.md)

## Discussion

Call this method to let the system know that the user is performing the associated activity. The system makes this object the current user activity object, which makes it available for Handoff and search indexing. If another user activity object was previously active, that object is made inactive.

Don’t call this method when providing a user activity object for a Siri request. Siri holds on to user activity objects and passes them along to your app automatically in response to specific events.

If you previously called the [`invalidate()`](./invalidate%28%29.md) method on the current object, calling this method has no effect.

## See Also

### Registering and invalidating activities
- [func resignCurrent()](./resigncurrent%28%29.md)
  Marks this activity object as inactive without invalidating it.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates an activity and marks it as no longer eligible for continuation.
- [var needsSave: Bool](./needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](./deleteallsaveduseractivities%28completionhandler%29.md)
  Deletes all user activities created by your app.
- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](./deletesaveduseractivities%28withpersistentidentifiers,completionhandler%29.md)
  Deletes user activities created by your app that have the specified persistent identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/becomecurrent())*