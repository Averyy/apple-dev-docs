# CPMapTemplate

**Framework**: CarPlay  
**Kind**: class

A template that displays a navigation overlay that your app draws on the map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPMapTemplate
```

#### Overview

After CarPlay calls your scene delegate’s [`templateApplicationScene(_:didConnect:to:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md) method, create a map template and set it as the root template by calling [`setRootTemplate(_:animated:completion:)`](cpinterfacecontroller/setroottemplate(_:animated:completion:).md) on the interface controller the method provides.

The map template appears as an overlay on top of the base view. The template is the control layer, providing a navigation bar and map buttons that users interact with through the CarPlay screen.

> **Note**:  The base view is where your app draws its map. CarPlay doesn’t support direct user interactions in this view. Instead, your app uses templates, which overlay the base view, to allow users to interact with your app through the CarPlay screen.

 The base view is where your app draws its map. CarPlay doesn’t support direct user interactions in this view. Instead, your app uses templates, which overlay the base view, to allow users to interact with your app through the CarPlay screen.

When the user begins to interact with your app through the CarPlay screen, the system displays the navigation bar, hiding it after a brief period of inactivity. You can change this behavior by setting the [`automaticallyHidesNavigationBar`](cpmaptemplate/automaticallyhidesnavigationbar.md) and [`hidesButtonsWithNavigationBar`](cpmaptemplate/hidesbuttonswithnavigationbar.md) properties.

The navigation bar includes up to two leading and two trailing buttons. You can change the buttons, including their titles and icon images, by setting the [`leadingNavigationBarButtons`](cpbarbuttonproviding/leadingnavigationbarbuttons.md) and [`trailingNavigationBarButtons`](cpbarbuttonproviding/trailingnavigationbarbuttons.md) properties on your template.

You can display additional map buttons by providing an array of [`CPMapButton`](cpmapbutton.md) objects to [`mapButtons`](cpmaptemplate/mapbuttons.md). Use these buttons to provide users access to actions, such as entering panning mode or zooming in and out on the map.

## Topics

### Configuring Map Templates
- [var automaticallyHidesNavigationBar: Bool](cpmaptemplate/automaticallyhidesnavigationbar.md)
  A Boolean value that indicates whether the template should automatically hide the navigation bar.
- [var hidesButtonsWithNavigationBar: Bool](cpmaptemplate/hidesbuttonswithnavigationbar.md)
  A Boolean value that tells the system to hide the map buttons when hiding the navigation bar.
- [var guidanceBackgroundColor: UIColor](cpmaptemplate/guidancebackgroundcolor.md)
  The background color the map template uses when displaying guidance.
### Handling Map Template Events
- [var mapDelegate: (any CPMapTemplateDelegate)?](cpmaptemplate/mapdelegate.md)
  The object that serves as the delegate of the map template.
- [protocol CPMapTemplateDelegate](cpmaptemplatedelegate.md)
  The protocol an object implements to handle events from a map template.
### Managing Map Buttons
- [var mapButtons: [CPMapButton]](cpmaptemplate/mapbuttons.md)
  An array of map buttons on the trailing bottom corner of the map template.
- [class CPMapButton](cpmapbutton.md)
  A button that represents an action that a map template displays on the CarPlay screen.
### Displaying Trip Previews
- [func showTripPreviews([CPTrip], textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:textconfiguration:).md)
  Displays the preview for one or more trips, and allows route selection.
- [func showTripPreviews([CPTrip], selectedTrip: CPTrip?, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:selectedtrip:textconfiguration:).md)
  Displays the previews for a collection of trips, with a single selected trip.
- [func hideTripPreviews()](cpmaptemplate/hidetrippreviews.md)
  Hides the display of trip previews.
- [func showRouteChoicesPreview(for: CPTrip, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showroutechoicespreview(for:textconfiguration:).md)
  Displays the route choices for a single trip.
- [class CPTripPreviewTextConfiguration](cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.
### Navigating a Trip
- [func startNavigationSession(for: CPTrip) -> CPNavigationSession](cpmaptemplate/startnavigationsession(for:).md)
  Begins navigational guidance for a trip.
- [class CPNavigationSession](cpnavigationsession.md)
  An object that represents an active route guidance session.
### Providing Trip Estimates
- [func updateEstimates(CPTravelEstimates, for: CPTrip)](cpmaptemplate/updateestimates(_:for:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip.
- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](cpmaptemplate/update(_:for:with:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [enum CPTimeRemainingColor](cptimeremainingcolor.md)
  The color the system uses when displaying the time remaining for a trip.
- [var tripEstimateStyle: CPTripEstimateStyle](cpmaptemplate/tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.
- [enum CPTripEstimateStyle](cptripestimatestyle.md)
  The set of display styles for trip estimates.
### Displaying a Navigation Alert
- [func present(navigationAlert: CPNavigationAlert, animated: Bool)](cpmaptemplate/present(navigationalert:animated:).md)
  Displays a navigation alert on the map template.
- [func dismissNavigationAlert(animated: Bool, completion: (Bool) -> Void)](cpmaptemplate/dismissnavigationalert(animated:completion:).md)
  Tells the map template to dismiss the visable navigation alert.
- [var currentNavigationAlert: CPNavigationAlert?](cpmaptemplate/currentnavigationalert.md)
  The visible navigation alert.
- [class CPNavigationAlert](cpnavigationalert.md)
  An alert that displays map- or navigation-related information to the user.
### Panning the Map
- [func showPanningInterface(animated: Bool)](cpmaptemplate/showpanninginterface(animated:).md)
  Shows the panning interface on the map.
- [func dismissPanningInterface(animated: Bool)](cpmaptemplate/dismisspanninginterface(animated:).md)
  Dismisses the panning interface.
- [var isPanningInterfaceVisible: Bool](cpmaptemplate/ispanninginterfacevisible.md)
  A Boolean value that indicates whether the map template is displaying the panning interface.

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CPBarButtonProviding](cpbarbuttonproviding.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Integrating CarPlay with Your Navigation App](integrating-carplay-with-your-navigation-app.md)
  Configure your navigation app to work with CarPlay by displaying your custom map and directions.
- [class CPTemplateApplicationDashboardScene](cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [protocol CPTemplateApplicationDashboardSceneDelegate](cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [class CPSearchTemplate](cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate)*