# TipKit

**Framework**: TipKit  
**Kind**: module

Display tips that help people discover features in your app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 10.0+

#### Overview

Use TipKit to show contextual tips that highlight new, interesting, or unused features people haven’t discovered on their own yet.

![A conceptual image showing general tips added to general apps.](https://docs-assets.developer.apple.com/published/ad49c41b987c8654c79823101b5defd9/tipkit_hero%402x.png)

Define your tip content, and the conditions under which they appear, with the [`Tip`](tip.md) protocol. Then draw attention to new features using the [`TipView`](tipview.md).

As you design tips for your app, ensure you don’t overwhelm your users. Use tips sparingly to highlight nonobvious features people haven’t discovered on their own. Similarly, avoid displaying tips each time someone uses your app. Tips can become distracting when they appear unnecessarily. Don’t use tips to guide people through your app, or for advertising and promotion purposes.

For design guidance on tips, see [`Human Interface Guidelines > Offering help`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/offering-help).

> **Note**: Session 10229: [`Make features discoverable with TipKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10229/)

Session 10229: [`Make features discoverable with TipKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10229/)

```swift
import SwiftUI
import TipKit

// Define your tip's content.
struct FavoriteLandmarkTip: Tip {
    var title: Text {
        Text("Save as a Favorite")
    }

    var message: Text? {
        Text("Your favorite landmarks always appear at the top of the list.")
    }

    var image: Image? {
        Image(systemName: "star")
    }
}

@main
struct LandmarkTips: App {
    // Create an instance of your tip.
    var favoriteLandmarkTip = FavoriteLandmarkTip()

    var body: some Scene {
        WindowGroup {
            VStack {
                // Place the tip view near the feature you want to highlight.
                TipView(favoriteLandmarkTip, arrowEdge: .bottom)

                Image(systemName: "star")
                    .imageScale(.large)
                Spacer()
            }
            .task {
                // Configure and load your tips at app launch.
                do {
                    try Tips.configure()
                } 
                catch {
                    // Handle TipKit errors
                    print("Error initializing TipKit \(error.localizedDescription)")
                }
            }
        }
    }
}
```

## Topics

### Essentials
- [Highlighting app features with TipKit](highlightingappfeatureswithtipkit.md)
  Bring attention to new features in your app by using tips.
### Content
- [protocol Tip](tip.md)
  A type that sets a tip’s content, as well as the conditions for when it displays.
- [class TipGroup](tipgroup.md)
  A collection of tips that can be presented one at a time using a specific order or based on the first tip eligible for display.
### Configuration
- [static func configure([Tips.ConfigurationOption]) throws](tips/configure(_:).md)
  Loads and configures the persistent state of all tips in your app.
- [static func cloudKitContainer(Tips.ConfigurationOption.CloudKitContainer?) -> Tips.ConfigurationOption](tips/configurationoption/cloudkitcontainer(_:).md)
  Sets the CloudKit container used for syncing tips.
- [static func datastoreLocation(Tips.ConfigurationOption.DatastoreLocation) -> Tips.ConfigurationOption](tips/configurationoption/datastorelocation(_:).md)
  Specify a custom location for your tips datastore.
- [static func displayFrequency(Tips.ConfigurationOption.DisplayFrequency) -> Tips.ConfigurationOption](tips/configurationoption/displayfrequency(_:).md)
  Customizes how often new tips are presented in your app after another tip has been displayed.
### Views
- [struct TipView](tipview.md)
  A user interface element that represents an inline tip.
- [@MainActor @preconcurrency func popoverTip(_ tip: (any Tip)?, arrowEdge: Edge? = nil, action: @escaping (Tips.Action) -> Void = { _ in }) -> some View
](../SwiftUI/View/popoverTip(_:arrowEdge:action:).md)
  Presents a popover tip on the modified view.
### UIKit Views
- [class TipUIView](tipuiview.md)
  A user interface element that represents a tip in UIKit applications.
- [class TipUIPopoverViewController](tipuipopoverviewcontroller.md)
  A view controller that displays a popover tip in UIKit applications.
- [class TipUICollectionViewCell](tipuicollectionviewcell.md)
  A collection view cell that embeds a tip.
- [class TipUICollectionReusableView](tipuicollectionreusableview.md)
  A UICollectionReusableView subclass that represents a tip.
### AppKit Views
- [class TipNSView](tipnsview.md)
  A user interface element that represents a tip in AppKit applications.
- [class TipNSPopover](tipnspopover.md)
  A subclass of NSPopover that displays a popover tip in AppKit applications.
### Display rules
- [struct Rule](tips/rule.md)
  A condition to meet before displaying a tip.
- [struct Parameter](tips/parameter.md)
  A type that monitors the state of its wrapped value to reevaluate any dependent tip rules when the value changes.
- [struct Event](tips/event.md)
  A repeatable user-defined action.
### View Style
- [@MainActor @preconcurrency func tipViewStyle(_ style: some TipViewStyle) -> some View
](../SwiftUI/View/tipViewStyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [protocol TipViewStyle](tipviewstyle.md)
  A type that applies custom appearance to all tips within a view hierarchy.
- [struct TipViewStyleConfiguration](tipviewstyleconfiguration.md)
  The container type that holds a tip’s configuration.
- [struct MiniTipViewStyle](minitipviewstyle.md)
  The default style for a TipView.
### Testing
- [static func showAllTipsForTesting()](tips/showalltipsfortesting.md)
  Show all tips regardless of their display rule eligibility or display frequency status for UI testing of tips.
- [static func showTipsForTesting([any Tip.Type])](tips/showtipsfortesting(_:).md)
  Show specified tips regardless of their display rule eligibility or display frequency status for UI testing of certain tips.
- [static func hideAllTipsForTesting()](tips/hidealltipsfortesting.md)
  Hide all tips regardless of their display rule eligibility for UI testing without tips.
- [static func hideTipsForTesting([any Tip.Type])](tips/hidetipsfortesting(_:).md)
  Hide specified tips regardless of their display rule eligibility for UI testing without certain tips.
- [static func resetDatastore() throws](tips/resetdatastore.md)
  Resets the tips’ datastore to the initial state for re-testing tip display rules and eligibility.
### Errors
- [struct TipKitError](tipkiterror.md)
  A localized tip kit error.
### Common types
- [struct AnyTip](anytip.md)
  A type-erased tip value.
- [protocol TipOption](tipoption.md)
  A type that represents the various customizations that you can make to a tip’s behavior.
### Enumerations
- [enum Tips](tips.md)
  TipKit namespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TipKit)*