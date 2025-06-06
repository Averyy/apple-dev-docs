# SFAddToHomeScreenActivityItem

**Framework**: Safari Services  
**Kind**: protocol

A protocol that describes a bookmark someone can add to their Home Screen.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol SFAddToHomeScreenActivityItem : NSObjectProtocol
```

#### Overview

To add a bookmark to someone’s Home Screen from your browser app, create an object that conforms to [`SFAddToHomeScreenActivityItem`](sfaddtohomescreenactivityitem.md) and present a [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController) that includes the activity item.

If your browser app uses WebKit, [`SFAddToHomeScreenActivityItem`](sfaddtohomescreenactivityitem.md) always represents a bookmark. To let someone add a web app to their Home Screen, add a [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) to the [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController) activity items instead of a [`SFAddToHomeScreenActivityItem`](sfaddtohomescreenactivityitem.md). WebKit inspects the website’s metadata to decide whether the item represents a bookmark or a web app.

If your browser app includes an alternative browser engine, pass detailed information about the bookmark to [`getHomeScreenWebAppInfo(completionHandler:)`](sfaddtohomescreenactivityitem/gethomescreenwebappinfo(completionhandler:).md). If the bookmark represents a web app, include the web app manifest, and cookies that the system uses when someone opens the web app from their Home Screen.

> ❗ **Important**:  [`SFAddToHomeScreenActivityItem`](sfaddtohomescreenactivityitem.md) is only available to web browsers. For more information on creating a web browser, see [`Preparing your app to be the default web browser`](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser).

 [`SFAddToHomeScreenActivityItem`](sfaddtohomescreenactivityitem.md) is only available to web browsers. For more information on creating a web browser, see [`Preparing your app to be the default web browser`](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser).

## Topics

### Describing a bookmark or web app
- [var iconItemProvider: NSItemProvider?](sfaddtohomescreenactivityitem/iconitemprovider.md)
  An object that conveys the bookmark’s icon to the system.
- [var title: String](sfaddtohomescreenactivityitem/title.md)
  The bookmark’s title.
- [var url: URL](sfaddtohomescreenactivityitem/url.md)
  The bookmark’s URL.
### Providing information about a web app to the system
- [func getHomeScreenWebAppInfo(completionHandler: (SFAddToHomeScreenInfo?) -> Void)](sfaddtohomescreenactivityitem/gethomescreenwebappinfo(completionhandler:).md)
  Provides information about a web app to the system.
- [class SFAddToHomeScreenInfo](sfaddtohomescreeninfo.md)
  A class that provides information about a web app that someone adds to their Home Screen.
- [func getWebAppManifest(completionHandler: (BEWebAppManifest?) -> Void)](sfaddtohomescreenactivityitem/getwebappmanifest(completionhandler:).md)
  Provides the web app’s manifest to the system, if the bookmark represents a web app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem)*