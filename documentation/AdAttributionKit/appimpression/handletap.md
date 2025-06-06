# handleTap()

**Framework**: AdAttributionKit  
**Kind**: method

Processes click-through interactions on your custom rendered ad content.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
func handleTap() async throws
```

## Mentions

- [Presenting ads in your app](presenting-ads-in-your-app.md)

#### Discussion

Handle a person tapping your ad content by calling the app impression’s handle tap method.

If the system can validate that  person tapped, it attempts to either launch one of the installed marketplaces to show the product page to install the advertised app, or it performs a reengagement if someone already has the advertised app installed, and opens it directly.

This API requires that you place a [`UIEventAttributionView`](https://developer.apple.com/documentation/UIKit/UIEventAttributionView) on top of your ad content before calling `handleTap()`, as the following example shows:

```swift
   func handleAdTapped(impression: AppImpression) async {
       do {
           // This fails if a person didn't tap a `UIEventAttributionView`.
           try await impression.handleTap()
       }
       catch {
           print("Failed to perform click-through impression: \(error).")
       }
   }    
```

> **Note**: This method is only available for 15 minutes after you create the `impression`. After 15 minutes, you need to initialize a new `AppImpression` instance if you want to use the click-through ad API. This limitation doesn’t apply to view-through ads. For more information on view-through and click-through ads, see [`Presenting ads in your app`](presenting-ads-in-your-app.md).

This method is only available for 15 minutes after you create the `impression`. After 15 minutes, you need to initialize a new `AppImpression` instance if you want to use the click-through ad API. This limitation doesn’t apply to view-through ads. For more information on view-through and click-through ads, see [`Presenting ads in your app`](presenting-ads-in-your-app.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/handletap())*