# MCBrowserViewController

**Framework**: Multipeer Connectivity  
**Kind**: class  
**Role**: Class

The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ([`prepare(for:sender:)`](../UIKit/uiviewcontroller/prepare%28for,sender%29.md) and [`performSegue(withIdentifier:sender:)`](../UIKit/uiviewcontroller/performsegue%28withidentifier,sender%29.md) for storyboards or [`present(_:animated:completion:)`](../UIKit/uiviewcontroller/present%28_,animated,completion%29.md) and [`dismiss(animated:completion:)`](../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](../AppKit/nsviewcontroller/presentassheet%28_%29.md) and [`dismiss(_:)`](../AppKit/nsviewcontroller/dismiss%28_%29-91my5.md) instead.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
class MCBrowserViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface MCBrowserViewController : UIViewController
```

*macOS*

```objc
@interface MCBrowserViewController : NSViewController
```

## Topics

### Initializing a Browser View Controller
- [convenience init(serviceType: String, session: MCSession)](./mcbrowserviewcontroller/init%28servicetype,session%29.md)
  Initializes a browser view controller using the provided service type and session.
- [init(browser: MCNearbyServiceBrowser, session: MCSession)](./mcbrowserviewcontroller/init%28browser,session%29.md)
  Initializes a browser view controller with the provided browser and session.
- [var delegate: (any MCBrowserViewControllerDelegate)?](./mcbrowserviewcontroller/delegate.md)
  The delegate object that handles browser-view-controller-related events.
- [var browser: MCNearbyServiceBrowser?](./mcbrowserviewcontroller/browser.md)
  The browser object that is used for discovering peers.
- [var session: MCSession](./mcbrowserviewcontroller/session.md)
  The multipeer session to which the invited peers are connected.
### Getting and Setting the Maximum and Minimum Number of Peers
- [var maximumNumberOfPeers: Int](./mcbrowserviewcontroller/maximumnumberofpeers.md)
  The maximum number of peers allowed in a session, including the local peer.
- [var minimumNumberOfPeers: Int](./mcbrowserviewcontroller/minimumnumberofpeers.md)
  The minimum number of peers that need to be in a session, including the local peer.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MCNearbyServiceBrowserDelegate](./mcnearbyservicebrowserdelegate.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
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

### Classes
- [class MCAdvertiserAssistant](./mcadvertiserassistant.md)
  The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.
- [class MCNearbyServiceAdvertiser](./mcnearbyserviceadvertiser.md)
  The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.
- [class MCNearbyServiceBrowser](./mcnearbyservicebrowser.md)
  Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).
- [class MCPeerID](./mcpeerid.md)
  An  `MCPeerID` object represents a peer in a multipeer session.
- [class MCSession](./mcsession.md)
  An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)*