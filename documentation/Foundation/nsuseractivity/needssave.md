# needsSave

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the delegate for this user activity receives a [`userActivityWillSave(_:)`](nsuseractivitydelegate/useractivitywillsave(_:).md) callback before the activity is sent for continuation on another device.

## See Also

- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var requiredUserInfoKeys: Set<String>?](nsuseractivity/requireduserinfokeys.md)
  A set of keys that represent the minimal information about the activity that should be stored for later restoration.
- [var userInfo: [AnyHashable : Any]?](nsuseractivity/userinfo.md)
  A dictionary containing app-specific state information needed to continue an activity on another device.
- [func addUserInfoEntries(from: [AnyHashable : Any])](nsuseractivity/adduserinfoentries(from:).md)
  Adds the contents of the specified dictionary to the user info dictionary.
- [var targetContentIdentifier: String?](nsuseractivity/targetcontentidentifier.md)
  A string that identifies the user activity’s content.
- [var contentAttributeSet: CSSearchableItemAttributeSet?](nsuseractivity/contentattributeset.md)
  A set of properties that describe the activity.
- [var keywords: Set<String>](nsuseractivity/keywords.md)
  A set of localized keywords that can help users find the activity in search results.
- [var persistentIdentifier: NSUserActivityPersistentIdentifier?](nsuseractivity/persistentidentifier.md)
  A value used to identify the user activity.
- [typealias NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md)
  The type that defines a persistent identifier value for a user activity.
- [var appClipActivationPayload: APActivationPayload?](nsuseractivity/appclipactivationpayload.md)
  An object containing the payload information that launches an App Clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/needssave)*