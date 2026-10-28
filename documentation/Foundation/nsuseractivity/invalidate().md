# invalidate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) invalidate;
```

## Discussion

Call this method when the user stops engaging in the associated activity and that activity is no longer available. For example, you might call this method when the user closes the window associated with the activity. After calling this method on a user activity object, calling the [`becomeCurrent()`](./becomecurrent%28%29.md) method on that object has no effect.

## See Also

### Registering and invalidating activities
- [func becomeCurrent()](./becomecurrent%28%29.md)
  Marks the activity as currently in use by the user.
- [func resignCurrent()](./resigncurrent%28%29.md)
  Marks this activity object as inactive without invalidating it.
- [var needsSave: Bool](./needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](./deleteallsaveduseractivities%28completionhandler%29.md)
  Deletes all user activities created by your app.
- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](./deletesaveduseractivities%28withpersistentidentifiers,completionhandler%29.md)
  Deletes user activities created by your app that have the specified persistent identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/invalidate())*