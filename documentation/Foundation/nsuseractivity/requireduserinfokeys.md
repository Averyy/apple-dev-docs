# requiredUserInfoKeys

**Framework**: Foundation  
**Kind**: property

A set of keys that represent the minimal information about the activity that should be stored for later restoration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var requiredUserInfoKeys: Set<String>? { get set }
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Discussion

The keys come from the [`userInfo`](nsuseractivity/userinfo.md) property.

## See Also

- [var userInfo: [AnyHashable : Any]?](nsuseractivity/userinfo.md)
  A dictionary containing app-specific state information needed to continue an activity on another device.
- [func addUserInfoEntries(from: [AnyHashable : Any])](nsuseractivity/adduserinfoentries(from:).md)
  Adds the contents of the specified dictionary to the user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/requireduserinfokeys)*