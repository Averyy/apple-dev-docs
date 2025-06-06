# SKCloudServiceSetupViewController

**Framework**: StoreKit  
**Kind**: class

A view controller that helps people perform setup for a cloud service, like an Apple Music subscription.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class SKCloudServiceSetupViewController
```

## Mentions

- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md)
- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)

#### Overview

Use the view that this view controller presents to allow customers to set up cloud services that are associated with their iTunes Store account, like an Apple Music subscription.

To enable the Apple Music subscriber setup flow in particular, you first request the current set of capabilities from [`SKCloudServiceController`](skcloudservicecontroller.md). Then, present the setup view controller only when the [`musicCatalogSubscriptionEligible`](skcloudservicecapability/musiccatalogsubscriptioneligible.md) capability is enabled and the [`musicCatalogPlayback`](skcloudservicecapability/musiccatalogplayback.md) capability is disabled.

For information about other capabilities that you can enable by using this view controller, see [`SKCloudServiceCapability`](skcloudservicecapability.md).

## Topics

### Setting a delegate
- [var delegate: (any SKCloudServiceSetupViewControllerDelegate)?](skcloudservicesetupviewcontroller/delegate.md)
  The cloud service view controller’s delegate.
- [protocol SKCloudServiceSetupViewControllerDelegate](skcloudservicesetupviewcontrollerdelegate.md)
  A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed.
### Loading the setup view
- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md)
  Allow eligible customers to subscribe to Apple Music.
- [struct SKCloudServiceSetupOptionsKey](skcloudservicesetupoptionskey.md)
  Keys to specify the types of setup options for a cloud service.
- [func load(options: [SKCloudServiceSetupOptionsKey : Any], completionHandler: ((Bool, (any Error)?) -> Void)?)](skcloudservicesetupviewcontroller/load(options:completionhandler:).md)
  Loads the cloud service setup view with the specified options.
- [class SKArcadeService](skarcadeservice.md)

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class SKCloudServiceController](skcloudservicecontroller.md)
  An object that determines the current capabilities of a person’s Music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller)*