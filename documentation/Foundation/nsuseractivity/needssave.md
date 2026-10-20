# needsSave

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the state of the activity needs to be updated.

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
var needsSave: Bool { get set }
```

```objc
@property (assign) BOOL needsSave;
```

#### Discussion

If [`true`](../../Swift/true.md), the delegate for this user activity receives a [`userActivityWillSave(_:)`](../nsuseractivitydelegate/useractivitywillsave%28_%29.md) callback before the activity is sent for continuation on another device.

## See Also

### Registering and invalidating activities
- [func becomeCurrent()](./becomecurrent%28%29.md)
  Marks the activity as currently in use by the user.
- [func resignCurrent()](./resigncurrent%28%29.md)
  Marks this activity object as inactive without invalidating it.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates an activity and marks it as no longer eligible for continuation.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](./deleteallsaveduseractivities%28completionhandler%29.md)
  Deletes all user activities created by your app.
- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](./deletesaveduseractivities%28withpersistentidentifiers,completionhandler%29.md)
  Deletes user activities created by your app that have the specified persistent identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/needssave)*