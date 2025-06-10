# CarPlay

**Framework**: CarPlay  
**Kind**: module

Integrate CarPlay in apps related to audio, communication, navigation, parking, EV charging, food ordering, and more.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

#### Overview

Use the CarPlay framework to create an in-car experience for your app. The framework provides templates for building a version of your app’s interface suitable for presentation on a vehicle’s displays. Add the templates you want to your app and customize them to suit your content. You control the content of the templates, but the framework controls certain aspects of the template interface elements, such as the touch target size, font size, font color, and highlights.

CarPlay features run when the current device supports CarPlay and when that device is connected to an appropriately equipped vehicle. CarPlay handles variations in vehicle systems, letting you focus on your content. When a person runs your app from their vehicle, the system generates and hosts your app’s interface for you. If the device doesn’t support CarPlay, the system doesn’t try to access your app’s CarPlay features.

You can use other technologies to drive portions of your app’s CarPlay interface. Messaging apps can include [`SiriKit`](https://developer.apple.com/documentation/SiriKit) support to allow someone to read or send messages. VoIP apps can use [`CallKit`](https://developer.apple.com/documentation/CallKit) to manage incoming and outgoing calls, often in combination with SiriKit call support. Navigation apps can include [`MapKit`](https://developer.apple.com/documentation/MapKit) support.

> **Note**:  Session 10635: [`Accelerate Your App with CarPlay`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10635/)

## Topics

### CarPlay Integration
- [Requesting CarPlay Entitlements](requesting-carplay-entitlements.md)
  Configure your CarPlay-enabled app with the entitlements it requires.
- [Displaying Content in CarPlay](displaying-content-in-carplay.md)
  Use scenes to present your app’s content on the vehicle’s built-in screen.
- [Supporting Previous Versions of iOS](supporting-previous-versions-of-ios.md)
  Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [Using the CarPlay Simulator](using-the-carplay-simulator.md)
  Configure Simulator to run and debug your CarPlay-enabled app.
- [class CPTemplateApplicationScene](cptemplateapplicationscene.md)
  A CarPlay scene that controls your app’s user interface.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.
- [class CPSessionConfiguration](cpsessionconfiguration.md)
  An object that provides vehicle properties and configuration for the CarPlay environment.
### General Purpose Templates
- [class CPListTemplate](cplisttemplate.md)
  A template that displays and manages a list of items.
- [class CPGridTemplate](cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPTabBarTemplate](cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPTemplate](cptemplate.md)
  An abstract base class for interface templates.
- [protocol CPBarButtonProviding](cpbarbuttonproviding.md)
  The methods that templates use to provide buttons for the navigation bar.
### Audio
- [Integrating CarPlay with Your Music App](integrating-carplay-with-your-music-app.md)
  Configure your music app to work with CarPlay by displaying a custom UI.
- [class CPNowPlayingTemplate](cpnowplayingtemplate.md)
  A shared system template that displays Now Playing information.
### Instrument cluster
- [class CPInstrumentClusterController](cpinstrumentclustercontroller.md)
- [protocol CPInstrumentClusterControllerDelegate](cpinstrumentclustercontrollerdelegate.md)
- [class CPTemplateApplicationInstrumentClusterScene](cptemplateapplicationinstrumentclusterscene.md)
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](cptemplateapplicationinstrumentclusterscenedelegate.md)
### Navigation
- [Integrating CarPlay with Your Navigation App](integrating-carplay-with-your-navigation-app.md)
  Configure your navigation app to work with CarPlay by displaying your custom map and directions.
- [class CPTemplateApplicationDashboardScene](cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [protocol CPTemplateApplicationDashboardSceneDelegate](cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [class CPMapTemplate](cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPSearchTemplate](cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
### Location and Information
- [class CPPointOfInterestTemplate](cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPInformationTemplate](cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [class CPTextButton](cptextbutton.md)
  A button that displays a stylized title.
- [Integrating CarPlay with your quick-ordering app](integrating-carplay-with-your-quick-ordering-app.md)
  Configure your food-ordering app to work with CarPlay.
### Maneuvers
- [class CPManeuver](cpmaneuver.md)
  An object that describes a single navigation instruction.
- [enum CPManeuverState](cpmaneuverstate.md)
  Values that describe the state of a maneuver.
- [enum CPManeuverType](cpmaneuvertype.md)
  Values that describe types of navigation maneuvers.
### Routes, lanes and junctions
- [class CPRouteInformation](cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPLane](cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [class CPLaneGuidance](cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPLaneStatus](cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPJunctionType](cpjunctiontype.md)
  Values that represent types of roadway junctions.
### Communication
- [class CPContactTemplate](cpcontacttemplate.md)
  A template that displays information about a person or a business.
### Actions and Alerts
- [class CPActionSheetTemplate](cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](cpalerttemplate.md)
  A template that displays a modal alert.
- [class CPAlertAction](cpalertaction.md)
  An object that encapsulates an action the user can perform on an action sheet or alert.
### Related Types
- [class CPButton](cpbutton.md)
  A button that displays an image and invokes a handler when the user taps it.
- [class CPImageSet](cpimageset.md)
  Light and dark representations of an image.
- [let CarPlayErrorDomain: String](carplayerrordomain.md)
  The domain that CarPlay uses for any errors it provides.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Symbols that the CarPlay framework no longer supports.
### Reference
- [CarPlay Enumerations](carplay-enumerations.md)
- [CarPlay Constants](carplay-constants.md)
### Classes
- [class CPListImageRowItemCardElement](cplistimagerowitemcardelement.md)
- [class CPListImageRowItemCondensedElement](cplistimagerowitemcondensedelement.md)
- [class CPListImageRowItemElement](cplistimagerowitemelement.md)
  Abstract superclass for a a row item element object.
- [class CPListImageRowItemGridElement](cplistimagerowitemgridelement.md)
- [class CPListImageRowItemImageGridElement](cplistimagerowitemimagegridelement.md)
- [class CPListImageRowItemRowElement](cplistimagerowitemrowelement.md)
- [class CPMessageGridItemConfiguration](cpmessagegriditemconfiguration.md)
- [class CPNowPlayingMode](cpnowplayingmode.md)
- [class CPNowPlayingModeSports](cpnowplayingmodesports.md)
  The sports mode represents a layout for now playing suited to live-streaming or recorded playback of a sporting event that features exactly two teams.
- [class CPNowPlayingSportsClock](cpnowplayingsportsclock.md)
  A representation of the amount of time elapsed so far in this event, for events where the clock counts UP.
- [class CPNowPlayingSportsEventStatus](cpnowplayingsportseventstatus.md)
  A representation of the status of a sporting event.
- [class CPNowPlayingSportsTeam](cpnowplayingsportsteam.md)
  A representation of a sports team for the now playing screen, in sports that have exactly two teams.
- [class CPNowPlayingSportsTeamLogo](cpnowplayingsportsteamlogo.md)
  A logo image or, if no image is available, an abbreviation or initialism for this team.
### Variables
- [let CPMaximumMessageItemLeadingDetailTextImageSize: CGSize](cpmaximummessageitemleadingdetailtextimagesize.md)
  Maximum size of an image for the detailed text leading image.
### Enumerations
- [enum CPListImageRowItemCondensedElementShape](cplistimagerowitemcondensedelementshape.md)
  Types of shape used to draw a condensed row element.
- [enum CPListImageRowItemImageGridElementShape](cplistimagerowitemimagegridelementshape.md)
  Types of shape used to draw a list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CarPlay)*