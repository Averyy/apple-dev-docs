# MCBrowserViewController

**Framework**: Multipeer Connectivity  
**Kind**: class

The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ([`prepare(for:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/prepare(for:sender:)) and [`performSegue(withIdentifier:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/performSegue(withIdentifier:sender:)) for storyboards or [`present(_:animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/present(_:animated:completion:)) and [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/presentAsSheet(_:)) and [`dismiss(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/dismiss(_:)-91my5) instead.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MCBrowserViewController
```

## Topics

### Initializing a Browser View Controller
- [convenience init(serviceType: String, session: MCSession)](mcbrowserviewcontroller/init(servicetype:session:).md)
  Initializes a browser view controller using the provided service type and session.
- [init(browser: MCNearbyServiceBrowser, session: MCSession)](mcbrowserviewcontroller/init(browser:session:).md)
  Initializes a browser view controller with the provided browser and session.
- [var delegate: (any MCBrowserViewControllerDelegate)?](mcbrowserviewcontroller/delegate.md)
  The delegate object that handles browser-view-controller-related events.
- [var browser: MCNearbyServiceBrowser?](mcbrowserviewcontroller/browser.md)
  The browser object that is used for discovering peers.
- [var session: MCSession](mcbrowserviewcontroller/session.md)
  The multipeer session to which the invited peers are connected.
### Getting and Setting the Maximum and Minimum Number of Peers
- [var maximumNumberOfPeers: Int](mcbrowserviewcontroller/maximumnumberofpeers.md)
  The maximum number of peers allowed in a session, including the local peer.
- [var minimumNumberOfPeers: Int](mcbrowserviewcontroller/minimumnumberofpeers.md)
  The minimum number of peers that need to be in a session, including the local peer.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MCNearbyServiceBrowserDelegate](mcnearbyservicebrowserdelegate.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
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

- [class MCAdvertiserAssistant](mcadvertiserassistant.md)
  The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.
- [class MCNearbyServiceAdvertiser](mcnearbyserviceadvertiser.md)
  The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.
- [class MCNearbyServiceBrowser](mcnearbyservicebrowser.md)
  Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).
- [class MCPeerID](mcpeerid.md)
  An  `MCPeerID` object represents a peer in a multipeer session.
- [class MCSession](mcsession.md)
  An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)*