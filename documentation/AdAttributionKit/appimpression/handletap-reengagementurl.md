# handleTap(reengagementURL:)

**Framework**: AdAttributionKit  
**Kind**: method

Processes click-through interactions on your custom rendered ad content, and delivers a URL to the advertised app if it’s installed.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+

## Declaration

```swift
func handleTap(reengagementURL: URL) async throws
```

#### Discussion

Use this method to provide a URL to deeply link someone into an advertised app if they have the app installed.

If the system can validate that a person tapped the custom rendered ad content, it attempts to either launch one of the installed marketplaces to show the product page to install the advertised app, or performs a reengagement if the advertised app is already installed, and opens the reengagement URL.

AdAttributionKit requires the URL to be a universal link specifically for the advertised app that the framework uses at runtime to attempt to open the app. If the URL isn’t a universal link, or the universal link isn’t registered to the advertised app, the framework disregards the URL and launches the app as usual without passing the URL. For more information, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content) and [`Supporting universal links in your app`](https://developer.apple.com/documentation/Xcode/supporting-universal-links-in-your-app).

## Parameters

- `reengagementURL`: A universal link into the advertised app that the framework attempts to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/handletap(reengagementurl:))*