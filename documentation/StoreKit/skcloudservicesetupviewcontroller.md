# SKCloudServiceSetupViewController

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

A view controller that helps people perform setup for a cloud service, like an Apple Music subscription.

**Availability**:
- iOS 10.1+ - Deprecated in 18.0
- iPadOS 10.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0

> **Deprecated**: Use [`musicSubscriptionOffer(isPresented:options:onLoadCompletion:)`](../SwiftUI/view/musicsubscriptionoffer%28ispresented,options,onloadcompletion%29.md) instead.

## Declaration

```swift
@MainActor
class SKCloudServiceSetupViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface SKCloudServiceSetupViewController : UIViewController
```

*macOS*

```objc
@interface SKCloudServiceSetupViewController : NSViewController
```

## Mentions

- [Offering Apple Music Subscription in Your App](./offering-apple-music-subscription-in-your-app.md)
- [Determining a person’s Apple Music capabilities](./determining-a-person-s-apple-music-capabilities.md)

#### Overview

Use the view that this view controller presents to allow customers to set up cloud services that are associated with their iTunes Store account, like an Apple Music subscription.

To enable the Apple Music subscriber setup flow in particular, you first request the current set of capabilities from [`SKCloudServiceController`](./skcloudservicecontroller.md). Then, present the setup view controller only when the [`musicCatalogSubscriptionEligible`](./skcloudservicecapability/musiccatalogsubscriptioneligible.md) capability is enabled and the [`musicCatalogPlayback`](./skcloudservicecapability/musiccatalogplayback.md) capability is disabled.

For information about other capabilities that you can enable by using this view controller, see [`SKCloudServiceCapability`](./skcloudservicecapability.md).

## Topics

### Setting a delegate
- [var delegate: (any SKCloudServiceSetupViewControllerDelegate)?](./skcloudservicesetupviewcontroller/delegate.md)
  The cloud service view controller’s delegate.
- [protocol SKCloudServiceSetupViewControllerDelegate](./skcloudservicesetupviewcontrollerdelegate.md)
  A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed.
### Loading the setup view
- [Offering Apple Music Subscription in Your App](./offering-apple-music-subscription-in-your-app.md)
  Allow eligible customers to subscribe to Apple Music.
- [struct SKCloudServiceSetupOptionsKey](./skcloudservicesetupoptionskey.md)
  Keys to specify the types of setup options for a cloud service.
- [func load(options: [SKCloudServiceSetupOptionsKey : Any], completionHandler: ((Bool, (any Error)?) -> Void)?)](./skcloudservicesetupviewcontroller/load%28options,completionhandler%29.md)
  Loads the cloud service setup view with the specified options.
- [class SKArcadeService](./skarcadeservice.md)

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
- [NSViewController](../AppKit/nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Deprecated
- [class SKCloudServiceController](./skcloudservicecontroller.md)
  An object that determines the current capabilities of a person’s Music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller)*