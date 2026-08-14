# SKStoreProductViewController

**Framework**: StoreKit  
**Kind**: class

A view controller that provides a page where customers can purchase media from the App Store.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
class SKStoreProductViewController
```

## Mentions

- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)
- [Signing and providing ads](signing-and-providing-ads.md)

#### Overview

To display a store for customers to purchase media from the App Store, follow these steps:

1. Create an `SKStoreProductViewController` object and set its [`delegate`](skstoreproductviewcontroller/delegate.md).
2. Indicate a specific product to sell by passing its iTunes item identifier to the [`loadProduct(withParameters:completionBlock:)`](skstoreproductviewcontroller/loadproduct(withparameters:completionblock:).md) method.
3. Present the view controller modally from another view controller in your app. Your delegate dismisses the view controller when the customer completes the purchase.

Present the `SKStoreProductViewController` object immediately when someone triggers an interaction, such as tapping a Buy button. Load the product information before presenting the view controller to ensure a seamless user experience.

This class ignores [`modalPresentationStyle`](https://developer.apple.com/documentation/uikit/uiviewcontroller/modalpresentationstyle) settings, and those settings have no impact on the sheet’s presentation.

To recommend another app without displaying a full product page, and to recommend an App Clip’s corresponding app from within the App Clip, use [`SKOverlay`](skoverlay.md).

> **Note**:  In a compatible iPad or iPhone app running in visionOS, this method displays a minimal sheet to enable an app purchase or to launch the App Store for more information. For an in-line experience that’s consistent across platforms, use [`SKOverlay`](skoverlay.md) instead.

##### Prevent Exceptions

The `SKStoreProductViewController` class doesn’t support subclassing or embedding, and must be used as-is.

> ❗ **Important**:  If you compile with the iOS 13 SDK, attempting to instantiate a subclass of `SKStoreProductViewController` results in a runtime exception.

This class throws the following runtime exceptions:

- **SKUnsupportedClassException**: Occurs if the app attempts to instantiate a subclass of `SKStoreProductViewController`.
- **SKUnsupportedPresentationException**: Occurs if the app attempts to use an unsupported presentation mode for `SKStoreProductViewController`, such as embedding it as a subview controller or attempting to use it in a popover.

## Topics

### Setting a delegate
- [var delegate: (any SKStoreProductViewControllerDelegate)?](skstoreproductviewcontroller/delegate.md)
  The store view controller’s delegate.
- [protocol SKStoreProductViewControllerDelegate](skstoreproductviewcontrollerdelegate.md)
  A protocol to call when the customer dismisses the store screen.
### Loading a new product screen
- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md)
  Allow users to purchase media in the App Store from within your app.
- [func loadProduct(withParameters: [String : Any], completionBlock: ((Bool, (any Error)?) -> Void)?)](skstoreproductviewcontroller/loadproduct(withparameters:completionblock:).md)
  Loads a new product screen to display.
- [func loadProduct(withParameters: [String : Any], impression: SKAdImpression, completionBlock: ((Bool, (any Error)?) -> Void)?)](skstoreproductviewcontroller/loadproduct(withparameters:impression:completionblock:).md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression) async throws](skstoreproductviewcontroller/loadproduct(parameters:impression:).md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression, reengagementURL: URL) async throws](skstoreproductviewcontroller/loadproduct(parameters:impression:reengagementurl:).md)
- [Product Dictionary Keys](product-dictionary-keys.md)
  Keys for identifying products and the tokens for affiliates and campaigns.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md)
  Allow users to purchase media in the App Store from within your app.
- [class SKOverlay](skoverlay.md)
  A class that displays an overlay you can use to recommend another app or an App Clip’s corresponding full app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)*