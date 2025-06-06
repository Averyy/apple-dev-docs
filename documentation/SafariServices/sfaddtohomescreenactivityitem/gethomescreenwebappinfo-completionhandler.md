# getHomeScreenWebAppInfo(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Provides information about a web app to the system.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- visionOS 2.2+

## Declaration

```swift
optional func homeScreenWebAppInfo() async -> SFAddToHomeScreenInfo?
```

#### Overview

Add information about the web app to a [`SFAddToHomeScreenInfo`](sfaddtohomescreeninfo.md) object that you create, and pass it to the completion handler.

The system only calls this method in browser apps that include an alternative browser engine. If you implement this method, then the system doesn’t call your implementation of [`getWebAppManifest(completionHandler:)`](sfaddtohomescreenactivityitem/getwebappmanifest(completionhandler:).md).

## Parameters

- `completionHandler`: A closure that you call to supply the web app’s information to the system.

## See Also

- [class SFAddToHomeScreenInfo](sfaddtohomescreeninfo.md)
  A class that provides information about a web app that someone adds to their Home Screen.
- [func getWebAppManifest(completionHandler: (BEWebAppManifest?) -> Void)](sfaddtohomescreenactivityitem/getwebappmanifest(completionhandler:).md)
  Provides the web app’s manifest to the system, if the bookmark represents a web app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem/gethomescreenwebappinfo(completionhandler:))*