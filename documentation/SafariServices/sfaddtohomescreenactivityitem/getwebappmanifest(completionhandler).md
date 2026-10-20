# getWebAppManifest(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Provides the web app’s manifest to the system, if the bookmark represents a web app.

**Availability**:
- iOS 17.5+ - Deprecated in 27.2
- iPadOS 17.5+ - Deprecated in 27.2
- Mac Catalyst 17.5+ - Deprecated in 27.2
- visionOS 1.2+ - Deprecated in 27.2

> **Deprecated**: Create a SFAddToHomeScreenInfo instead

## Declaration

```swift
optional func getWebAppManifest(completionHandler: @escaping @Sendable (BEWebAppManifest?) -> Void)
```

```swift
optional func webAppManifest() async -> BEWebAppManifest?
```

```objc
- (void) getWebAppManifestWithCompletionHandler:(void (^)(BEWebAppManifest *)) completionHandler;
```

#### Discussion

The system only calls this method in browser apps that include an alternative browser engine.

## Parameters

- `completionHandler`: A closure that you call to supply the web app manifest to the system.

## See Also

### Providing information about a web app to the system
- [func getHomeScreenWebAppInfo(completionHandler: (SFAddToHomeScreenInfo?) -> Void)](./gethomescreenwebappinfo%28completionhandler%29.md)
  Provides information about a web app to the system.
- [class SFAddToHomeScreenInfo](../sfaddtohomescreeninfo.md)
  A class that provides information about a web app that someone adds to their Home Screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem/getwebappmanifest(completionhandler:))*