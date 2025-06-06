# init()

**Framework**: Foundation  
**Kind**: init

Creates a user activity object using the first activity type declared in the app’s information property list file.

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
convenience init()
```

#### Return Value

An [`NSUserActivity`](nsuseractivity.md) object.

#### Discussion

This method retrieves the first string of the [`NSUserActivityTypes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW28) key declared in the app’s `Info.plist` file.

## See Also

- [Creating a user activity object](creating-a-user-activity-object.md)
  Identify key user interactions and include the information to restore them later.
- [init(activityType: String)](nsuseractivity/init(activitytype:).md)
  Creates a user activity object with the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/init())*