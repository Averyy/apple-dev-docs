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

- [var userInfo: [AnyHashable : Any]?](nsuseractivity/userinfo.md)
  A dictionary containing app-specific state information needed to continue an activity on another device.
- [var requiredUserInfoKeys: Set<String>?](nsuseractivity/requireduserinfokeys.md)
  A set of keys that represent the minimal information about the activity that should be stored for later restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/adduserinfoentries(from:))*