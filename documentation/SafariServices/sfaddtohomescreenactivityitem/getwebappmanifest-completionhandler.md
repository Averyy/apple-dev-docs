# getWebAppManifest(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Provides the web app’s manifest to the system, if the bookmark represents a web app.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 1.2+

## Declaration

```swift
optional func webAppManifest() async -> BEWebAppManifest?
```

#### Discussion

The system only calls this method in browser apps that include an alternative browser engine.

## Parameters

- `completionHandler`: A closure that you call to supply the web app manifest to the system.

## See Also

- [func getHomeScreenWebAppInfo(completionHandler: (SFAddToHomeScreenInfo?) -> Void)](sfaddtohomescreenactivityitem/gethomescreenwebappinfo(completionhandler:).md)
  Provides information about a web app to the system.
- [class SFAddToHomeScreenInfo](sfaddtohomescreeninfo.md)
  A class that provides information about a web app that someone adds to their Home Screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem/getwebappmanifest(completionhandler:))*