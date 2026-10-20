# CPMapTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The protocol an object implements to handle events from a map template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol CPMapTemplateDelegate : NSObjectProtocol
```

```objc
@protocol CPMapTemplateDelegate <NSObject>
```

## Topics

### Setting the Display Style
- [func mapTemplate(CPMapTemplate, displayStyleFor: CPManeuver) -> CPManeuverDisplayStyle](./cpmaptemplatedelegate/maptemplate%28_,displaystylefor%29.md)
  Asks the delegate for the maneuver’s display style.
- [struct CPManeuverDisplayStyle](./cpmaneuverdisplaystyle.md)
  A display style that determines the visual layout for a maneuver.
### Handling Navigation Events
- [func mapTemplate(CPMapTemplate, selectedPreviewFor: CPTrip, using: CPRouteChoice)](./cpmaptemplatedelegate/maptemplate%28_,selectedpreviewfor,using%29.md)
  Tells the delegate that the user selected a trip and route choice to preview.
- [func mapTemplate(CPMapTemplate, startedTrip: CPTrip, using: CPRouteChoice)](./cpmaptemplatedelegate/maptemplate%28_,startedtrip,using%29.md)
  Tells the delegate that the user selected a trip and route choice to navigate.
- [func mapTemplateDidCancelNavigation(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatedidcancelnavigation%28_%29.md)
  Tells the delegate that the system canceled the navigation.
- [func mapTemplateShouldProvideNavigationMetadata(CPMapTemplate) -> Bool](./cpmaptemplatedelegate/maptemplateshouldprovidenavigationmetadata%28_%29.md)
  Asks the delegate whether the template should provide navigation metadata
### Displaying Notifications
- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPManeuver) -> Bool](./cpmaptemplatedelegate/maptemplate%28_,shouldshownotificationfor%29-4mnm1.md)
  Asks the delegate whether the system should display the maneuver as a notification when the app is in the background.
- [func mapTemplate(CPMapTemplate, shouldUpdateNotificationFor: CPManeuver, with: CPTravelEstimates) -> Bool](./cpmaptemplatedelegate/maptemplate%28_,shouldupdatenotificationfor,with%29.md)
  Asks the delegate whether the system should display the maneuver with updated travel estimates as a notification when the app is in the background.
- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPNavigationAlert) -> Bool](./cpmaptemplatedelegate/maptemplate%28_,shouldshownotificationfor%29-5lu8a.md)
  Asks the delegate whether the system should display the navigation alert as a notification when the app is in the background.
### Handling Navigation Alerts
- [func mapTemplate(CPMapTemplate, willShow: CPNavigationAlert)](./cpmaptemplatedelegate/maptemplate%28_,willshow%29.md)
  Tells the delegate that the system will show the navigation alert.
- [func mapTemplate(CPMapTemplate, didShow: CPNavigationAlert)](./cpmaptemplatedelegate/maptemplate%28_,didshow%29.md)
  Tells the delegate that the system showed the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./cpmaptemplatedelegate/maptemplate%28_,willdismiss,dismissalcontext%29.md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [func mapTemplate(CPMapTemplate, didDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](./cpmaptemplatedelegate/maptemplate%28_,diddismiss,dismissalcontext%29.md)
  Tells the delegate that the system dismissed the navigation alert.
- [CPNavigationAlert.DismissalContext](./cpnavigationalert/dismissalcontext.md)
  A set of reasons for dismissing a navigation alert.
### Panning the Map
- [func mapTemplateDidShowPanningInterface(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatedidshowpanninginterface%28_%29.md)
  Tells the delegate that the panning interface is visible on the map.
- [func mapTemplateWillDismissPanningInterface(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatewilldismisspanninginterface%28_%29.md)
  Tells the delegate that the panning interface will disappear from the map.
- [func mapTemplateDidDismissPanningInterface(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatediddismisspanninginterface%28_%29.md)
  Tells the delegate that the panning interface is no longer visible on the map.
- [func mapTemplateDidBeginPanGesture(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatedidbeginpangesture%28_%29.md)
  Tells the delegate that the pan gesture has started.
- [func mapTemplate(CPMapTemplate, panBeganWith: CPMapTemplate.PanDirection)](./cpmaptemplatedelegate/maptemplate%28_,panbeganwith%29.md)
  Tells the delegate that the user is starting to pan the map.
- [func mapTemplate(CPMapTemplate, panWith: CPMapTemplate.PanDirection)](./cpmaptemplatedelegate/maptemplate%28_,panwith%29.md)
  Tells the delegate that the user is panning in a certain direction on the map.
- [func mapTemplate(CPMapTemplate, panEndedWith: CPMapTemplate.PanDirection)](./cpmaptemplatedelegate/maptemplate%28_,panendedwith%29.md)
  Tells the delegate that the user stopped panning the map.
- [CPMapTemplate.PanDirection](./cpmaptemplate/pandirection.md)
  The directions a user can pan (or move) a map displayed on the CarPlay screen.
- [func mapTemplate(CPMapTemplate, didEndPanGestureWithVelocity: CGPoint)](./cpmaptemplatedelegate/maptemplate%28_,didendpangesturewithvelocity%29.md)
  Tells the delegate that the pan gesture ended with the specified velocity.
- [func mapTemplate(CPMapTemplate, didUpdatePanGestureWithTranslation: CGPoint, velocity: CGPoint)](./cpmaptemplatedelegate/maptemplate%28_,didupdatepangesturewithtranslation,velocity%29.md)
  Tells the delegate that the pan gesture changed.
### Instance Methods
- [func mapTemplate(CPMapTemplate, didEndZoomGestureWithVelocity: CGFloat)](./cpmaptemplatedelegate/maptemplate%28_,didendzoomgesturewithvelocity%29.md)
  Tells the delegate that a person stopped zooming the map.
- [func mapTemplate(CPMapTemplate, didFailToShareDestinationFor: CPTrip, error: any Error)](./cpmaptemplatedelegate/maptemplate%28_,didfailtosharedestinationfor,error%29.md)
  Called when a vehicle failed to handle a shared trip’s destination
- [func mapTemplate(CPMapTemplate, didReceiveRequestForDestination: CPNavigationWaypoint)](./cpmaptemplatedelegate/maptemplate%28_,didreceiverequestfordestination%29.md)
  Called when a navigation request is received. Show a trip preview corresponding to this destination and start navigation if the destination is accepted by the user.
- [func mapTemplate(CPMapTemplate, didReceiveUpdatedRouteSource: CPRouteSource)](./cpmaptemplatedelegate/maptemplate%28_,didreceiveupdatedroutesource%29.md)
  Called when the route source status has been updated by the built-in system.
- [func mapTemplate(CPMapTemplate, didRequestMultiStopCardConfigurationWithCompletion: (CPMultiStopCardConfiguration) -> Void)](./cpmaptemplatedelegate/maptemplate%28_,didrequestmultistopcardconfigurationwithcompletion%29.md)
  Called when the user requests multi-stop card to be displayed via tapping ETA tray.
- [func mapTemplate(CPMapTemplate, didRequestToInsert: CPNavigationWaypoint, into: CPRouteSegment, completion: (CPTravelEstimates) -> Void)](./cpmaptemplatedelegate/maptemplate%28_,didrequesttoinsert,into,completion%29.md)
  Called when the built-in navigation system sends a waypoint to the device for a specific segment.
- [func mapTemplate(CPMapTemplate, didRequestToRemove: CPNavigationWaypoint)](./cpmaptemplatedelegate/maptemplate%28_,didrequesttoremove%29.md)
  Called when the user removes a waypoint. Perform a reroute to update the route accordingly.
- [func mapTemplate(CPMapTemplate, didRequestToRemoveDestination: CPNavigationWaypoint)](./cpmaptemplatedelegate/maptemplate%28_,didrequesttoremovedestination%29.md)
  Called when the user removes the waypoint corresponding to the trip’s destination. Perform a reroute to update both the trip and route accordingly.
- [func mapTemplate(CPMapTemplate, didRotateWithCenter: CGPoint, rotation: CGFloat, velocity: CGFloat)](./cpmaptemplatedelegate/maptemplate%28_,didrotatewithcenter,rotation,velocity%29.md)
  Tells the delegate that a person is rotating the map.
- [func mapTemplate(CPMapTemplate, didShareDestinationFor: CPTrip)](./cpmaptemplatedelegate/maptemplate%28_,didsharedestinationfor%29.md)
  Called when a vehicle successfully handled a shared trip’s destination
- [func mapTemplate(CPMapTemplate, didUpdateRouteSharingEnabled: Bool)](./cpmaptemplatedelegate/maptemplate%28_,didupdateroutesharingenabled%29.md)
  Called when the route sharing enabled status has been updated by the built-in system. Route sharing enabled is set to true when any vehicle features are enabled that rely on a route provided by the built‑in navigation system to func‑ tion.
- [func mapTemplate(CPMapTemplate, didUpdateZoomGestureWithCenter: CGPoint, scale: CGFloat, velocity: CGFloat)](./cpmaptemplatedelegate/maptemplate%28_,didupdatezoomgesturewithcenter,scale,velocity%29.md)
  Tells the delegate that a person is zooming on the map.
- [func mapTemplate(CPMapTemplate, pitchEndedWithCenter: CGPoint)](./cpmaptemplatedelegate/maptemplate%28_,pitchendedwithcenter%29.md)
  Tells the delegate that a person stopped pitching the map.
- [func mapTemplate(CPMapTemplate, pitchWithCenter: CGPoint)](./cpmaptemplatedelegate/maptemplate%28_,pitchwithcenter%29.md)
  Called when a pitch gesture changes. May not be called when connected to some CarPlay systems
- [func mapTemplate(CPMapTemplate, rotationDidEndWithVelocity: CGFloat)](./cpmaptemplatedelegate/maptemplate%28_,rotationdidendwithvelocity%29.md)
  Tells the delegate that a person stopped rotating the map.
- [func mapTemplate(CPMapTemplate, waypoint: CPNavigationWaypoint, accepted: Bool, forSegment: CPRouteSegment?)](./cpmaptemplatedelegate/maptemplate%28_,waypoint,accepted,forsegment%29.md)
  Called when the user responds to a proposal to add a waypoint as a stop on their route. If the waypoint is accepted, perform a reroute to update the route accordingly for the specified segment to include this new destination.
- [func mapTemplate(CPMapTemplate, willShareDestinationFor: CPTrip)](./cpmaptemplatedelegate/maptemplate%28_,willsharedestinationfor%29.md)
  Called when a trip’s destination is about to be shared to the vehicle
- [func mapTemplateDidBeginPitchGesture(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatedidbeginpitchgesture%28_%29.md)
  Tells the delegate that the pitch gesture started.
- [func mapTemplateDidBeginRotationGesture(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatedidbeginrotationgesture%28_%29.md)
  Tells the delegate that the rotation gesture started.
- [func mapTemplateDidBeginZoomGesture(CPMapTemplate)](./cpmaptemplatedelegate/maptemplatedidbeginzoomgesture%28_%29.md)
  Tells the delegate that the zoom gesture started.
- [func mapTemplateShouldProvideMultiStopRouting(CPMapTemplate) -> Bool](./cpmaptemplatedelegate/maptemplateshouldprovidemultistoprouting%28_%29.md)
  Determines if the template should provide UI for multi-stop routing while actively navigating, including the ability to add and remove stops.
- [func mapTemplateShouldProvideRouteSharing(CPMapTemplate) -> Bool](./cpmaptemplatedelegate/maptemplateshouldprovideroutesharing%28_%29.md)
  Determines if the template should provide route sharing information to the vehicle. Apps that participate in route sharing will donate navigation information to the vehicle including the current route, a list of waypoints, and other metadata that allows the vehicle to track the user’s preferred route to their destination.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling Map Template Events
- [var mapDelegate: (any CPMapTemplateDelegate)?](./cpmaptemplate/mapdelegate.md)
  The object that serves as the delegate of the map template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate)*