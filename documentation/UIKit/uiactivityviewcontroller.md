# UIActivityViewController

**Framework**: UIKit  
**Kind**: class

A view controller that you use to offer standard services from your app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIActivityViewController
```

## Mentions

- [Collaborating and sharing copies of your data](collaborating-and-sharing-copies-of-your-data.md)

#### Overview

The system provides several standard services, such as copying items to the pasteboard, posting content to social media sites, sending items via email or SMS, and more. Apps can also define custom services.

Your app is responsible for configuring, presenting, and dismissing this view controller. Configuration for the view controller involves specifying the data objects on which the view controller should act. (You can also specify the list of custom services your app supports.) When presenting the view controller, you must do so using the appropriate means for the current device. On iPad, you must present the view controller in a popover. On iPhone and iPod touch, you must present it modally.

## Topics

### Initializing the activity view controller
- [init(activityItems: [Any], applicationActivities: [UIActivity]?)](uiactivityviewcontroller/init(activityitems:applicationactivities:).md)
  Initializes a new activity view controller object that acts on the specified data.
- [convenience init(activityItemsConfiguration: any UIActivityItemsConfigurationReading)](uiactivityviewcontroller/init(activityitemsconfiguration:).md)
  Initializes a new activity view controller object that acts on the specified configuration.
- [class UIActivityItemsConfiguration](uiactivityitemsconfiguration.md)
  A configuration that allows a responder to export data through a variety of interactions.
- [protocol UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md)
  A set of methods adopted by an object so that the object can act as an activity items configuration.
### Accessing the completion handler
- [var completionWithItemsHandler: UIActivityViewController.CompletionWithItemsHandler?](uiactivityviewcontroller/completionwithitemshandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.
- [UIActivityViewController.CompletionWithItemsHandler](uiactivityviewcontroller/completionwithitemshandler-swift.typealias.md)
  A completion handler to execute after the activity view controller is dismissed.
### Excluding specific activity types
- [var excludedActivityTypes: [UIActivity.ActivityType]?](uiactivityviewcontroller/excludedactivitytypes.md)
  The list of services that should not be displayed.
### Excluding specific sections
- [var excludedActivitySectionTypes: UIActivitySectionTypes](uiactivityviewcontroller/excludedactivitysectiontypes.md)
- [struct UIActivitySectionTypes](uiactivitysectiontypes.md)
### Elevating a prominent activity
- [var allowsProminentActivity: Bool](uiactivityviewcontroller/allowsprominentactivity.md)
  A Boolean value the system uses to elevate a system activity to make it more prominent.
### Deprecated
- [var completionHandler: UIActivityViewController.CompletionHandler?](uiactivityviewcontroller/completionhandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.
- [UIActivityViewController.CompletionHandler](uiactivityviewcontroller/completionhandler-swift.typealias.md)
  A completion handler to execute after the activity view controller is dismissed.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIActivity](uiactivity.md)
  An abstract class that you subclass to implement app-specific services.
- [protocol UIActivityItemSource](uiactivityitemsource.md)
  A set of methods that an activity view controller uses to retrieve the data items to act on.
- [class UIActivityItemProvider](uiactivityitemprovider.md)
  A proxy for data that passes to an activity view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller)*