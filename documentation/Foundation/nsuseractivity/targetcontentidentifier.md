# targetContentIdentifier

**Framework**: Foundation  
**Kind**: property

A string that identifies the user activity’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var targetContentIdentifier: String? { get set }
```

#### Discussion

A target content identifier is a string you define within your app. This string provides a unique identifier for specific content in your app, like a particular document or the location of a piece of data in a database. This string isn’t visible to the user.

If you set this property, when the system delivers an [`NSUserActivity`](nsuseractivity.md) object to an app with multiple scenes, it chooses the [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) whose [`UISceneActivationConditions`](https://developer.apple.com/documentation/UIKit/UISceneActivationConditions) have the best match with the target content identifier. For more information, see [`UISceneActivationConditions`](https://developer.apple.com/documentation/UIKit/UISceneActivationConditions).

This property is optional but is highly recommended to create a great multitasking experience for apps that run on iPad. Setting this property doesn’t automatically set [`needsSave`](nsuseractivity/needssave.md) to [`true`](https://developer.apple.com/documentation/swift/true).

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
- [var needsSave: Bool](nsuseractivity/needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/targetcontentidentifier)*