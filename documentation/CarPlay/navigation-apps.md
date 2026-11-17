# Navigation

**Framework**: CarPlay  
**Role**: API Collection

Build an app that provides turn-by-turn directions to someone while driving.

## Overview

A navigation app provides turn-by-turn driving directions and information about upcoming maneuvers. Use this type of app to deliver your custom map content, and provide additional information on top of the map using the CarPlay map template and map panels. Navigation apps can offer route choices, multiple stops along the route, and guidance on the the best lane, road, or junction to take. Apps can also replicate most of this content in the vehicle’s instrument cluster or in the CarPlay dashboard using separate scenes.

This type of app supports the following CarPlay templates:

- [`CPMapTemplate`](./cpmaptemplate.md)

- [`CPContactTemplate`](./cpcontacttemplate.md)
- [`CPInformationTemplate`](./cpinformationtemplate.md)
- [`CPSearchTemplate`](./cpsearchtemplate.md)
- [`CPTabBarTemplate`](./cptabbartemplate.md)
- [`CPListTemplate`](./cplisttemplate.md)
- [`CPGridTemplate`](./cpgridtemplate.md)
- [`CPVoiceControlTemplate`](./cpvoicecontroltemplate.md)
- [`CPActionSheetTemplate`](./cpactionsheettemplate.md)
- [`CPAlertTemplate`](./cpalerttemplate.md)

## Topics

### Essentials
- [CarPlay Navigation app](../BundleResources/entitlements/com.apple.developer.carplay-maps.md)
  A Boolean value that indicates whether the CarPlay app provides turn-by-turn directions.
- [Integrating CarPlay with Your Navigation App](./integrating-carplay-with-your-navigation-app.md)
  Configure your navigation app to work with CarPlay by displaying your custom map and directions.
### Dashboard display
- [class CPDashboardController](./cpdashboardcontroller.md)
  A controller that provides shortcut buttons for the CarPlay Dashboard.
- [class CPDashboardButton](./cpdashboardbutton.md)
  A shortcut button for placement on the CarPlay Dashboard.
- [class CPTemplateApplicationDashboardScene](./cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [protocol CPTemplateApplicationDashboardSceneDelegate](./cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [CPSupportsDashboardNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsdashboardnavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.
### Instrument cluster display
- [class CPTemplateApplicationInstrumentClusterScene](./cptemplateapplicationinstrumentclusterscene.md)
  A CarPlay scene that presents navigation-related instructions in the vehicle’s instrument display.
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](./cptemplateapplicationinstrumentclusterscenedelegate.md)
  The methods for responding to the life cycle events in your app’s instrument cluster scene.
- [class CPInstrumentClusterController](./cpinstrumentclustercontroller.md)
  The controller you use to configure and manage your instrument cluster interface.
- [protocol CPInstrumentClusterControllerDelegate](./cpinstrumentclustercontrollerdelegate.md)
  The methods for responding to changes to instrument cluster settings.
- [enum CPInstrumentClusterSetting](./cpinstrumentclustersetting.md)
  Constants that indicate when to include or exclude vehicle-related data in your custom content.
- [CPSupportsInstrumentClusterNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.
### Session management
- [class CPNavigationSession](./cpnavigationsession.md)
  An object that represents an active route guidance session.
### Trip and waypoints
- [class CPTrip](./cptrip.md)
  An object that represents a journey between an origin and a destination.
- [class CPMapTemplateWaypoint](./cpmaptemplatewaypoint.md)
  CPMapTemplateWaypoint represents a waypoint with associated travel estimates
- [class CPNavigationWaypoint](./cpnavigationwaypoint.md)
  CPNavigationWaypoint represents a point of interest along a route that provides location-based information and guidance.
- [class CPMultiStopCardConfiguration](./cpmultistopcardconfiguration.md)
### Route details
- [class CPRouteChoice](./cproutechoice.md)
  A possible route for a trip.
- [class CPRouteInformation](./cprouteinformation.md)
  A class that describes the characteristic elements of a route.
- [class CPRouteDetail](./cproutedetail.md)
- [class CPRouteSegment](./cproutesegment.md)
  CPRouteSegment describes information pertaining to a segment of a route.
- [enum CPRerouteReason](./cpreroutereason.md)
  Values that represent reasons for navigation rerouting.
- [enum CPRouteSource](./cproutesource.md)
- [func NSStringFromCPRerouteReason(CPRerouteReason) -> String!](./nsstringfromcpreroutereason%28_%29.md)
### Maneuvers
- [class CPManeuver](./cpmaneuver.md)
  An object that describes a single navigation instruction.
- [enum CPManeuverState](./cpmaneuverstate.md)
  Values that describe the state of a maneuver.
- [enum CPManeuverType](./cpmaneuvertype.md)
  Values that describe types of navigation maneuvers.
- [class CPTravelEstimates](./cptravelestimates.md)
  An object that describes the time and distance remaining for a maneuver in a navigation session.
- [class CPTripPreviewTextConfiguration](./cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.
- [func NSStringFromCPManeuverType(CPManeuverType) -> String!](./nsstringfromcpmaneuvertype%28_%29.md)
- [struct CPLocationCoordinate3D](./cplocationcoordinate3d.md)
  CPLocationCoordinate3D represents a three-dimensional coordinate with latitude, longitude, and altitude components.
### Lanes and junctions
- [class CPLane](./cplane.md)
  A class that describes characteristics of a lane on a roadway.
- [class CPLaneGuidance](./cplaneguidance.md)
  A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- [enum CPLaneStatus](./cplanestatus.md)
  Values that describe the status or preferability of a lane.
- [enum CPJunctionType](./cpjunctiontype.md)
  Values that represent types of roadway junctions.
- [enum CPTrafficSide](./cptrafficside.md)
  Values that represent which side of the road the traffic drives on.
- [func NSStringFromCPJunctionType(CPJunctionType) -> String!](./nsstringfromcpjunctiontype%28_%29.md)
- [func NSStringFromCPLaneStatus(CPLaneStatus) -> String!](./nsstringfromcplanestatus%28_%29.md)
- [func NSStringFromCPTrafficSide(CPTrafficSide) -> String!](./nsstringfromcptrafficside%28_%29.md)
### Navigation alerts
- [class CPNavigationAlert](./cpnavigationalert.md)
  An alert that displays map- or navigation-related information to the user.

## See Also

### CarPlay app types
- [Audio](./audio.md)
  Build an app that plays audio or video content.
- [Communication](./communication-apps.md)
  Build an app that offers SiriKit messaging or VoIP calling services.
- [Driving task](./driving-task.md)
  Build an app that helps people perform driving-related tasks.
- [EV charging](./ev-charging.md)
  Build an app that provides helpful information about nearby charging facilities.
- [Fueling](./fueling.md)
  Build an app that provides helpful information about nearby fueling stations.
- [Parking](./parking.md)
  Build an app that provides helpful information about nearby parking facilities.
- [Public safety](./public-safety.md)
  Build an app that offers public safety information to someone who’s driving.
- [Quick food ordering](./quick-food-ordering.md)
  Build an app that helps someone order food for pickup.
- [Video](./video.md)
  Build an app that plays video content exclusively.
- [Voice-based conversation](./voice-based-conversation.md)
  Build an app that responds to questions or requests and performs actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/navigation-apps)*