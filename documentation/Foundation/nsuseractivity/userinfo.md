# userInfo

**Framework**: Foundation  
**Kind**: property

A dictionary containing app-specific state information needed to continue an activity on another device.

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
var userInfo: [AnyHashable : Any]? { get set }
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Discussion

Each key and value must be of the following types: [`NSArray`](nsarray.md), [`NSData`](nsdata.md), [`NSDate`](nsdate.md), [`NSDictionary`](nsdictionary.md), [`NSNull`](nsnull.md), [`NSNumber`](nsnumber.md), [`NSSet`](nsset.md), [`NSString`](nsstring.md), or [`NSURL`](nsurl.md). The system may translate file scheme URLs that refer to iCloud documents to valid file URLs on a continuing device.

## See Also

- [func addUserInfoEntries(from: [AnyHashable : Any])](nsuseractivity/adduserinfoentries(from:).md)
  Adds the contents of the specified dictionary to the user info dictionary.
- [var requiredUserInfoKeys: Set<String>?](nsuseractivity/requireduserinfokeys.md)
  A set of keys that represent the minimal information about the activity that should be stored for later restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo)*