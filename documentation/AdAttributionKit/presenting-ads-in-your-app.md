# Presenting ads in your app

**Framework**: AdAttributionKit

Render different ad styles in your app.

#### Overview

AdAttributionKit and StoreKit provide several ways to display in-app ads so you can customize ad display based on your app’s ad positioning or other advertising goals.

The first step to presenting ads in your app is to initialize an [`AppImpression`](appimpression.md) with an impression in compact JSON Web Signature (JWS) format. For more information about generating JWS impressions, see [`Generating JWS impressions`](generating-jws-impressions.md)

#### Record View Through Impressions Using Custom Rendered Ads

Custom rendered ads include content that overlays the app view. Record view-through impressions when your ad content has been displayed. To record a view-through impression, use the AdAttributionKit [`handleView()`](appimpression/handleview().md) method, as in the following SwiftUI example:

```swift
struct AdContentView: View {
    let impression: AppImpression

    var body: some View {
        VStack {
            // Advertisement content
        }
        .onDisappear(perform: { handleAdDisappeared() })
        .onTapGesture(perform: { handleAdTapped() })
    }


    init(impression: AppImpression) {
        self.impression = impression
    }


    func handleAdDisappeared() {
        guard shouldRecordView() else {
            return
        }
        
        Task {
            do {
                try await impression.handleView()
            }
            catch {
                print("Failed to end view through impression: \(error).")
            }
        }
    }
    
    func shouldRecordView() -> Bool {
        // TODO: Implement logic to determine if you need to record the view impression to your own system based on your app's ad display requirements.
        return false
    }
}
```

#### Record Click Through Impressions

To respond to a click-through interaction and redirect a person to open or install the advertised app, first display a [`UIEventAttributionView`](https://developer.apple.com/documentation/UIKit/UIEventAttributionView) over your ad content. Once the ad receives a tap, call [`handleTap()`](appimpression/handletap().md). The system then records a click-through impression, and if the app specified by the impression’s advertised item ID isn’t installed, the system launches the app’s product page on the App Store or alternative marketplace according to the user’s preferences in Settings. If the app is already installed, the system launches the app directly.

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

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/presenting-ads-in-your-app)*