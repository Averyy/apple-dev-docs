# Presenting ads in your app

**Framework**: Adattributionkit

Render different ad styles in your app.

#### Overview

AdAttributionKit and StoreKit provide several ways to display in-app ads so you can customize ad display based on your app’s ad positioning or other advertising goals.

The first step to presenting ads in your app is to initialize an [`AppImpression`](appimpression.md) with an impression in compact JSON Web Signature (JWS) format. For more information about generating JWS impressions, see [`Generating JWS impressions`](generating-jws-impressions.md)

#### Record View Through Impressions Using Custom Rendered Ads

Custom rendered ads include ad content that overlays the app view. To record a view-through impression use the AdAttributionKit [`beginView()`](appimpression/beginview().md) and [`endView()`](appimpression/endview().md) methods as shown in the following SwiftUI example using the `onAppear()` and `onDisappear()` view modifiers:

> **Note**: In UIKit, use the [`viewDidAppear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidAppear(_:)) and [`viewWillDisappear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewWillDisappear(_:)) methods. Don’t use or rely on timer methods to determine when to end an ad impression view in either SwiftUI or UIKit.

```swift
struct AdContentView: View {
    let impression: AppImpression

    var body: some View {
        VStack {
            // Advertisement content
        }
        .onAppear(perform: { handleAdAppeared() })
        .onDisappear(perform: { handleAdDisappeared() })
        .onTapGesture(perform: { handleAdTapped() })
    }

    init(impression: AppImpression) {
        self.impression = impression
    }

    func handleAdAppeared() {
        Task {
            do {
                try await impression.beginView()
            }
            catch {
                print("Failed to begin view through impression: \(error).")
            }
        }
    }

    func handleAdDisappeared() {
        Task {
            do {
                try await impression.endView()
            }
            catch {
                print("Failed to end view through impression: \(error).")
            }
        }
    }
}
```

#### Record Click Through Impressions and Redirect a Person to Open or Install the Advertised App

To respond to a click-through interaction, first display a [`UIEventAttributionView`](https://developer.apple.com/documentation/UIKit/UIEventAttributionView) over your ad content. Once the ad receives a tap, call [`handleTap()`](appimpression/handletap().md). The system then records a click-through impression, and if the app specified by the impression’s advertised item ID isn’t installed, the system launches the app’s product page on the App Store or alternative marketplace according to the user’s preferences in Settings. If the app is already installed, the system launches the app directly.

```swift
    func handleAdTapped(impression: AppImpression) async {
        do {
            // This fails if a person didn't tap `UIEventAttributionView`.
            try await impression.handleTap()
        }
        catch {
            print("Failed to perform click through impression: \(error).")
        }
    }
```

#### Display Storekit Rendered Ads

Pass an `AppImpression` when configuring a StoreKit rendered ad, and it handles recording a view-through impression after the framework displays it for 2 seconds; it records a click-through impression if a person taps through the ad. For more information on StoreKit rendered ads, see  [`SKStoreProductViewController`](https://developer.apple.com/documentation/StoreKit/SKStoreProductViewController), [`SKOverlay.AppConfiguration`](https://developer.apple.com/documentation/StoreKit/SKOverlay/AppConfiguration), [`appImpression`](https://developer.apple.com/documentation/StoreKit/SKOverlay/AppConfiguration/appImpression), and  [`loadProduct(parameters:impression:)`](https://developer.apple.com/documentation/StoreKit/SKStoreProductViewController/loadProduct(parameters:impression:))

## See Also

- [Understanding AdAttributionKit and SKAdNetwork interoperability](adattributionkit-skadnetwork-interoperability.md)
  Learn how attribution APIs interact to deliver ad impressions.
- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)
  Understand timeframes and priorities for ad impressions that result in ad attributions, and how impressions qualify for postbacks.
- [Identifying conversion values with conversion tags](conversion-tags.md)
  Use conversion tags to identify and update specific postbacks when you have overlapping conversion windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AdAttributionKit/presenting-ads-in-your-app)*