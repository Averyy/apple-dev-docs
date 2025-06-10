# UIEventAttributionView

**Framework**: UIKit  
**Kind**: class

An overlay view that verifies user interaction for Web AdAttributionKit.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIEventAttributionView
```

#### Overview

Web AdAttributionKit (formerly known as Private Click Measurement, or PCM) is a proposed web standard that allows external websites to measure when external links, such as ads, result in a . The external website decides what constitutes a conversion, but it’s often the result of the user making a purchase or signing up for a service. Web AdAttributionKit doesn’t send any user-identifiable information to the remote server, so it protects user privacy, while providing websites the ability to measure the effectiveness of their ad campaigns.

Apps running in iOS 17.4 or later can use [`AdAttributionKit`](https://developer.apple.com/documentation/AdAttributionKit) to record click-through impressions on custom rendered ad content using a `UIEventAttributionView`. For more information about click-through in AdAttributionKit, see [`Presenting ads in your app`](https://developer.apple.com/documentation/AdAttributionKit/presenting-ads-in-your-app).

Apps running in iOS 14.5 or later can take advantage of Web AdAttributionKit by sending event attribution data to the browser when opening an external link. If the linked website reports a conversion within 7 days, the browser forwards your appʼs Web AdAttributionKit data to a specified remote server sometime between 24 and 48 hours after the reported conversion.

You can’t subclass [`UIEventAttributionView`](uieventattributionview.md).

For more information on the proposed Web AdAttributionKit web standard, see [`Introducing Private Click Measurement`](https://developer.apple.comhttps://webkit.org/blog/11529/introducing-private-click-measurement-pcm/) and [`Private Click Measurement Draft Community Group Report`](https://developer.apple.comhttps://privacycg.github.io/private-click-measurement/).

##### Verify User Interaction

Event attribution views overlay other UIKit controls to ensure that either handling a tap with `AdAttributionKit` or opening an external link with Web AdAttributionKit data only happens as the result of a user tap. The system doesn’t handle the tap or send event attribution data to the browser unless a `UIEventAttributionView` exists above the tapped control.

##### Create an Event Attribution View

Place an event attribution view above any view that launches external links with event attribution data and make sure there are no other overlapping views above the event attribution view that might intercept taps. [`UIEventAttributionView`](uieventattributionview.md) doesn’t consume tap events, so the behavior of any control below one in the view hierarchy isn’t affected.

If multiple views or controls in your app can launch an external link using Web AdAttributionKit, use a separate [`UIEventAttributionView`](uieventattributionview.md) to overlay each control. While you can use a single [`UIEventAttributionView`](uieventattributionview.md) to validate more than one control, attribution views that cover large portions of the screen may impact performance because the system must validate all user interactions that pass through the attribution view.

Here’s how to add an event attribution view to an in-app advertisement:

For more information on sending Web AdAttributionKit event attribution data to the browser when opening an external link, see [`UIEventAttribution`](uieventattribution.md).

> **Note**:  Web AdAttributionKit isn’t supported in Mac apps built with Mac Catalyst.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIEventAttribution](uieventattribution.md)
  An object that contains event attribution information for Web AdAttributionKit.
- [NSAdvertisingAttributionReportEndpoint](../BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieventattributionview)*