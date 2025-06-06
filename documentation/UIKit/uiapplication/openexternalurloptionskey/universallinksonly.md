# universalLinksOnly

**Framework**: UIKit  
**Kind**: property

URLs must be universal links and have an app configured to open them.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let universalLinksOnly: UIApplication.OpenExternalURLOptionsKey
```

#### Discussion

When you include this key in the options dictionary of the [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md) method, the method opens the URL only if the URL is a valid universal link and there is an installed app capable of opening that URL. The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openexternalurloptionskey/universallinksonly)*