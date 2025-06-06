# becomeCurrent()

**Framework**: Foundation  
**Kind**: method

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

## Mentions

- [Creating a user activity object](creating-a-user-activity-object.md)

#### Discussion

Call this method to let the system know that the user is performing the associated activity. The system makes this object the current user activity object, which makes it available for Handoff and search indexing. If another user activity object was previously active, that object is made inactive.

Don’t call this method when providing a user activity object for a Siri request. Siri holds on to user activity objects and passes them along to your app automatically in response to specific events.

If you previously called the [`invalidate()`](nsuseractivity/invalidate().md) method on the current object, calling this method has no effect.

## See Also

- [func resignCurrent()](nsuseractivity/resigncurrent.md)
  Marks this activity object as inactive without invalidating it.
- [func invalidate()](nsuseractivity/invalidate.md)
  Invalidates an activity and marks it as no longer eligible for continuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/becomecurrent())*