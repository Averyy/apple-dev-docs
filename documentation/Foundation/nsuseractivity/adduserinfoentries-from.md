# addUserInfoEntries(from:)

**Framework**: Foundation  
**Kind**: method

Adds the contents of the specified dictionary to the user info dictionary.

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
func addUserInfoEntries(from otherDictionary: [AnyHashable : Any])
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Discussion

Use this method to add the keys from `otherDictionary` into the dictionary in the [`userInfo`](nsuseractivity/userinfo.md) property. If the same key is in both dictionaries, the value of the key is set to the value in the `otherDictionary` parameter.

It’s recommended that you keep the [`userInfo`](nsuseractivity/userinfo.md) dictionary as small as possible. The larger the dictionary, the longer it takes to deliver that payload and resume the activity.

## Parameters

- `otherDictionary`: The dictionary containing entries to be added.

## See Also

- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var requiredUserInfoKeys: Set<String>?](nsuseractivity/requireduserinfokeys.md)
  A set of keys that represent the minimal information about the activity that should be stored for later restoration.
- [var userInfo: [AnyHashable : Any]?](nsuseractivity/userinfo.md)
  A dictionary containing app-specific state information needed to continue an activity on another device.
- [var targetContentIdentifier: String?](nsuseractivity/targetcontentidentifier.md)
  A string that identifies the user activity’s content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/adduserinfoentries(from:))*