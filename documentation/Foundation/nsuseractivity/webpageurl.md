# webpageURL

**Framework**: Foundation  
**Kind**: property

The URL of the webpage to load in a browser to continue the activity.

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
var webpageURL: URL? { get set }
```

## Mentions

- [Creating a user activity object](creating-a-user-activity-object.md)

#### Discussion

When no suitable app is installed on a resuming device and the [`webpageURL`](nsuseractivity/webpageurl.md) property is set, the specified webpage is loaded and the user activity is continued in a web browser.

If your activity’s content can be restored on the web or you support Safari universal links, be sure to set this property so that the system can resume the activity in Safari or your app. After setting the [`webpageURL`](nsuseractivity/webpageurl.md) property on an activity for which [`isEligibleForSearch`](nsuseractivity/iseligibleforsearch.md) is [`true`](https://developer.apple.com/documentation/Swift/true), also set the [`requiredUserInfoKeys`](nsuseractivity/requireduserinfokeys.md) property, using the keys of the [`userInfo`](nsuseractivity/userinfo.md) dictionary that must be stored. If you don’t also set the [`requiredUserInfoKeys`](nsuseractivity/requireduserinfokeys.md) property, the [`userInfo`](nsuseractivity/userinfo.md) dictionary will be empty when the activity is restored.

If [`isEligibleForSearch`](nsuseractivity/iseligibleforsearch.md) is [`true`](https://developer.apple.com/documentation/Swift/true) for this activity and you’re using both [`NSUserActivity`](nsuseractivity.md) and web markup to index the same item, set [`webpageURL`](nsuseractivity/webpageurl.md) to the relevant URL on your website to avoid showing duplicate results in Spotlight. The [`NSUserActivity`](nsuseractivity.md) API does not perform any modifications to the URL that you specify. URL components, such as the query string and the fragment identifier, are used for matching the item against pages that are indexed by Applebot.

> **Note**:  The scheme of the [`webpageURL`](nsuseractivity/webpageurl.md) must be `http` or `https`. Any other scheme throws an exception.

## See Also

- [var referrerURL: URL?](nsuseractivity/referrerurl.md)
  The URL of the webpage that linked to the webpage URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/webpageurl)*