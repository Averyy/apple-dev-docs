# CPMapTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol

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

## Topics

### Setting the Display Style
- [func mapTemplate(CPMapTemplate, displayStyleFor: CPManeuver) -> CPManeuverDisplayStyle](cpmaptemplatedelegate/maptemplate(_:displaystylefor:).md)
  Asks the delegate for the maneuver’s display style.
- [struct CPManeuverDisplayStyle](cpmaneuverdisplaystyle.md)
  A display style that determines the visual layout for a maneuver.
### Handling Navigation Events
- [func mapTemplate(CPMapTemplate, selectedPreviewFor: CPTrip, using: CPRouteChoice)](cpmaptemplatedelegate/maptemplate(_:selectedpreviewfor:using:).md)
  Tells the delegate that the user selected a trip and route choice to preview.
- [func mapTemplate(CPMapTemplate, startedTrip: CPTrip, using: CPRouteChoice)](cpmaptemplatedelegate/maptemplate(_:startedtrip:using:).md)
  Tells the delegate that the user selected a trip and route choice to navigate.
- [func mapTemplateDidCancelNavigation(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidcancelnavigation(_:).md)
  Tells the delegate that the system canceled the navigation.
- [func mapTemplateShouldProvideNavigationMetadata(CPMapTemplate) -> Bool](cpmaptemplatedelegate/maptemplateshouldprovidenavigationmetadata(_:).md)
  Asks the delegate whether the template should provide navigation metadata
### Displaying Notifications
- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPManeuver) -> Bool](cpmaptemplatedelegate/maptemplate(_:shouldshownotificationfor:)-4mnm1.md)
  Asks the delegate whether the system should display the maneuver as a notification when the app is in the background.
- [func mapTemplate(CPMapTemplate, shouldUpdateNotificationFor: CPManeuver, with: CPTravelEstimates) -> Bool](cpmaptemplatedelegate/maptemplate(_:shouldupdatenotificationfor:with:).md)
  Asks the delegate whether the system should display the maneuver with updated travel estimates as a notification when the app is in the background.
- [func mapTemplate(CPMapTemplate, shouldShowNotificationFor: CPNavigationAlert) -> Bool](cpmaptemplatedelegate/maptemplate(_:shouldshownotificationfor:)-5lu8a.md)
  Asks the delegate whether the system should display the navigation alert as a notification when the app is in the background.
### Handling Navigation Alerts
- [func mapTemplate(CPMapTemplate, willShow: CPNavigationAlert)](cpmaptemplatedelegate/maptemplate(_:willshow:).md)
  Tells the delegate that the system will show the navigation alert.
- [func mapTemplate(CPMapTemplate, didShow: CPNavigationAlert)](cpmaptemplatedelegate/maptemplate(_:didshow:).md)
  Tells the delegate that the system showed the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](cpmaptemplatedelegate/maptemplate(_:willdismiss:dismissalcontext:).md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [func mapTemplate(CPMapTemplate, didDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](cpmaptemplatedelegate/maptemplate(_:diddismiss:dismissalcontext:).md)
  Tells the delegate that the system dismissed the navigation alert.
- [CPNavigationAlert.DismissalContext](cpnavigationalert/dismissalcontext.md)
  A set of reasons for dismissing a navigation alert.
### Panning the Map
- [func mapTemplateDidShowPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidshowpanninginterface(_:).md)
  Tells the delegate that the panning interface is visible on the map.
- [func mapTemplateWillDismissPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatewilldismisspanninginterface(_:).md)
  Tells the delegate that the panning interface will disappear from the map.
- [func mapTemplateDidDismissPanningInterface(CPMapTemplate)](cpmaptemplatedelegate/maptemplatediddismisspanninginterface(_:).md)
  Tells the delegate that the panning interface is no longer visible on the map.
- [func mapTemplateDidBeginPanGesture(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidbeginpangesture(_:).md)
  Tells the delegate that the pan gesture has started.
- [func mapTemplate(CPMapTemplate, panBeganWith: CPMapTemplate.PanDirection)](cpmaptemplatedelegate/maptemplate(_:panbeganwith:).md)
  Tells the delegate that the user is starting to pan the map.
- [func mapTemplate(CPMapTemplate, panWith: CPMapTemplate.PanDirection)](cpmaptemplatedelegate/maptemplate(_:panwith:).md)
  Tells the delegate that the user is panning in a certain direction on the map.
- [func mapTemplate(CPMapTemplate, panEndedWith: CPMapTemplate.PanDirection)](cpmaptemplatedelegate/maptemplate(_:panendedwith:).md)
  Tells the delegate that the user stopped panning the map.
- [CPMapTemplate.PanDirection](cpmaptemplate/pandirection.md)
  The directions a user can pan (or move) a map displayed on the CarPlay screen.
- [func mapTemplate(CPMapTemplate, didEndPanGestureWithVelocity: CGPoint)](cpmaptemplatedelegate/maptemplate(_:didendpangesturewithvelocity:).md)
  Tells the delegate that the pan gesture ended with the specified velocity.
- [func mapTemplate(CPMapTemplate, didUpdatePanGestureWithTranslation: CGPoint, velocity: CGPoint)](cpmaptemplatedelegate/maptemplate(_:didupdatepangesturewithtranslation:velocity:).md)
  Tells the delegate that the pan gesture changed.
### Instance Methods
- [func mapTemplate(CPMapTemplate, didEndZoomGestureWithVelocity: CGFloat)](cpmaptemplatedelegate/maptemplate(_:didendzoomgesturewithvelocity:).md)
  Tells the delegate that a person stopped zooming the map.
- [func mapTemplate(CPMapTemplate, didRotateWithCenter: CGPoint, rotation: CGFloat, velocity: CGFloat)](cpmaptemplatedelegate/maptemplate(_:didrotatewithcenter:rotation:velocity:).md)
  Tells the delegate that a person is rotating the map.
- [func mapTemplate(CPMapTemplate, didUpdateZoomGestureWithCenter: CGPoint, scale: CGFloat, velocity: CGFloat)](cpmaptemplatedelegate/maptemplate(_:didupdatezoomgesturewithcenter:scale:velocity:).md)
  Tells the delegate that a person is zooming on the map.
- [func mapTemplate(CPMapTemplate, pitchEndedWithCenter: CGPoint)](cpmaptemplatedelegate/maptemplate(_:pitchendedwithcenter:).md)
  Tells the delegate that a person stopped pitching the map.
- [func mapTemplate(CPMapTemplate, pitchWithCenter: CGPoint)](cpmaptemplatedelegate/maptemplate(_:pitchwithcenter:).md)
  Called when a pitch gesture changes. May not be called when connected to some CarPlay systems
- [func mapTemplate(CPMapTemplate, rotationDidEndWithVelocity: CGFloat)](cpmaptemplatedelegate/maptemplate(_:rotationdidendwithvelocity:).md)
  Tells the delegate that a person stopped rotating the map.
- [func mapTemplateDidBeginPitchGesture(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidbeginpitchgesture(_:).md)
  Tells the delegate that the pitch gesture started.
- [func mapTemplateDidBeginRotationGesture(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidbeginrotationgesture(_:).md)
  Tells the delegate that the rotation gesture started.
- [func mapTemplateDidBeginZoomGesture(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidbeginzoomgesture(_:).md)
  Tells the delegate that the zoom gesture started.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var mapDelegate: (any CPMapTemplateDelegate)?](cpmaptemplate/mapdelegate.md)
  The object that serves as the delegate of the map template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate)*