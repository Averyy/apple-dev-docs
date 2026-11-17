# CPMapTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays a navigation overlay that your app draws on the map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPMapTemplate
```

```objc
@interface CPMapTemplate : CPTemplate
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

After CarPlay calls your scene delegate’s [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method, create a map template and set it as the root template by calling [`setRootTemplate(_:animated:completion:)`](./cpinterfacecontroller/setroottemplate%28_,animated,completion%29.md) on the interface controller the method provides.

The map template appears as an overlay on top of the base view. The template is the control layer, providing a navigation bar and map buttons that users interact with through the CarPlay screen.

> **Note**:  The base view is where your app draws its map. CarPlay doesn’t support direct user interactions in this view. Instead, your app uses templates, which overlay the base view, to allow users to interact with your app through the CarPlay screen.

When the user begins to interact with your app through the CarPlay screen, the system displays the navigation bar, hiding it after a brief period of inactivity. You can change this behavior by setting the [`automaticallyHidesNavigationBar`](./cpmaptemplate/automaticallyhidesnavigationbar.md) and [`hidesButtonsWithNavigationBar`](./cpmaptemplate/hidesbuttonswithnavigationbar.md) properties.

The navigation bar includes up to two leading and two trailing buttons. You can change the buttons, including their titles and icon images, by setting the [`leadingNavigationBarButtons`](./cpbarbuttonproviding/leadingnavigationbarbuttons.md) and [`trailingNavigationBarButtons`](./cpbarbuttonproviding/trailingnavigationbarbuttons.md) properties on your template.

You can display additional map buttons by providing an array of [`CPMapButton`](./cpmapbutton.md) objects to [`mapButtons`](./cpmaptemplate/mapbuttons.md). Use these buttons to provide users access to actions, such as entering panning mode or zooming in and out on the map.

## Topics

### Configuring the map template
- [var automaticallyHidesNavigationBar: Bool](./cpmaptemplate/automaticallyhidesnavigationbar.md)
  A Boolean value that indicates whether the template should automatically hide the navigation bar.
- [var hidesButtonsWithNavigationBar: Bool](./cpmaptemplate/hidesbuttonswithnavigationbar.md)
  A Boolean value that tells the system to hide the map buttons when hiding the navigation bar.
- [var guidanceBackgroundColor: UIColor](./cpmaptemplate/guidancebackgroundcolor.md)
  The background color the map template uses when displaying guidance.
- [var mapButtons: [CPMapButton]](./cpmaptemplate/mapbuttons.md)
  An array of map buttons on the trailing bottom corner of the map template.
### Responding to map-related events
- [var mapDelegate: (any CPMapTemplateDelegate)?](./cpmaptemplate/mapdelegate.md)
  The object that serves as the delegate of the map template.
- [protocol CPMapTemplateDelegate](./cpmaptemplatedelegate.md)
  The protocol an object implements to handle events from a map template.
### Displaying trip previews
- [func showTripPreviews([CPTrip], textConfiguration: CPTripPreviewTextConfiguration?)](./cpmaptemplate/showtrippreviews%28_,textconfiguration%29.md)
  Displays the preview for one or more trips, and allows route selection.
- [func showTripPreviews([CPTrip], selectedTrip: CPTrip?, textConfiguration: CPTripPreviewTextConfiguration?)](./cpmaptemplate/showtrippreviews%28_,selectedtrip,textconfiguration%29.md)
  Displays the previews for a collection of trips, with a single selected trip.
- [func hideTripPreviews()](./cpmaptemplate/hidetrippreviews%28%29.md)
  Hides the display of trip previews.
- [func showRouteChoicesPreview(for: CPTrip, textConfiguration: CPTripPreviewTextConfiguration?)](./cpmaptemplate/showroutechoicespreview%28for,textconfiguration%29.md)
  Displays the route choices for a single trip.
- [class CPTripPreviewTextConfiguration](./cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.
### Providing trip estimates
- [func updateEstimates(CPTravelEstimates, for: CPTrip)](./cpmaptemplate/updateestimates%28_,for%29.md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip.
- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](./cpmaptemplate/update%28_,for,with%29.md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [enum CPTimeRemainingColor](./cptimeremainingcolor.md)
  The color the system uses when displaying the time remaining for a trip.
- [var tripEstimateStyle: CPTripEstimateStyle](./cpmaptemplate/tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.
- [enum CPTripEstimateStyle](./cptripestimatestyle.md)
  The set of display styles for trip estimates.
### Starting navigation for a trip
- [func startNavigationSession(for: CPTrip) -> CPNavigationSession](./cpmaptemplate/startnavigationsession%28for%29.md)
  Begins navigational guidance for a trip.
### Displaying navigation alerts
- [func present(navigationAlert: CPNavigationAlert, animated: Bool)](./cpmaptemplate/present%28navigationalert,animated%29.md)
  Displays a navigation alert on the map template.
- [func dismissNavigationAlert(animated: Bool, completion: (Bool) -> Void)](./cpmaptemplate/dismissnavigationalert%28animated,completion%29.md)
  Tells the map template to dismiss the visable navigation alert.
- [var currentNavigationAlert: CPNavigationAlert?](./cpmaptemplate/currentnavigationalert.md)
  The visible navigation alert.
### Displaying overlay panels
- [func showPanel(CPMapPanel, completion: ((Bool, (any Error)?) -> Void)?)](./cpmaptemplate/showpanel%28_,completion%29.md)
  Shows an overlay with the specified panel.
- [func hidePanel(completion: ((Bool, (any Error)?) -> Void)?)](./cpmaptemplate/hidepanel%28completion%29.md)
  Hides the overlay.
- [func pushPanel(CPMapPanel, completion: ((Bool, (any Error)?) -> Void)?)](./cpmaptemplate/pushpanel%28_,completion%29.md)
  Pushes a new panel.
- [func popPanel(completion: ((Bool, (any Error)?) -> Void)?)](./cpmaptemplate/poppanel%28completion%29.md)
  Pops the top panel from the overlay’s panel stack.
### Displaying the panning interface
- [func showPanningInterface(animated: Bool)](./cpmaptemplate/showpanninginterface%28animated%29.md)
  Shows the panning interface on the map.
- [func dismissPanningInterface(animated: Bool)](./cpmaptemplate/dismisspanninginterface%28animated%29.md)
  Dismisses the panning interface.
- [var isPanningInterfaceVisible: Bool](./cpmaptemplate/ispanninginterfacevisible.md)
  A Boolean value that indicates whether the map template is displaying the panning interface.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
### Conforms To
- [CPBarButtonProviding](./cpbarbuttonproviding.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interface templates
- [class CPTabBarTemplate](./cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPNowPlayingTemplate](./cpnowplayingtemplate.md)
  A shared system template that shows the currently selected audio content and offers controls to manage playback.
- [class CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPInformationTemplate](./cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [class CPContactTemplate](./cpcontacttemplate.md)
  A template that displays information about a person or a business.
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate)*