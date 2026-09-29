# ARCoachingOverlayView

**Framework**: ARKit  
**Kind**: class

A view that displays standardized onboarding instructions to direct users toward a specific goal.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class ARCoachingOverlayView
```

#### Overview

This view offers your users a standardized onboarding routine. You can configure this view to automatically display during session initialization and in limited tracking situations, while giving the user specific instructions that best facilitate ARKit’s world tracking.

These illustrations show overlay views with horizontal- and vertical-plane goals, indicating that the user should begin moving the device:

![Illustration showing two overlay views. The view at the left shows a horizontal plane, and the view at the right shows a vertical plane. Both views indicate that the user should begin moving the device.](/images/com.apple.arkit/media-3403212@2x.png)

These illustrations show overlay views indicating that the user should continue moving the phone or change the speed with which they move it:

![Illustration showing two overlay views. The view at the left indicates that the device is moving and the user should continue moving it. The view at the right indicates that the device is moving too fast and the user should move it more slowly.](/images/com.apple.arkit/media-3403211@2x.png)

When you start your app, the coaching overlay asks the user to move the device in ways that help ARKit establish tracking. When you choose a specific goal like finding a plane, the view tailors its instructions accordingly. After the coaching overlay determines the goal has been met and no further coaching is required, it hides from the user’s view.

For an example app that uses the coaching overlay, see [`Placing objects and handling 3D interaction`](placing-objects-and-handling-3d-interaction.md).

##### Supporting Automatic Coaching

By default, [`activatesAutomatically`](arcoachingoverlayview/activatesautomatically.md) is enabled and therefore you should override [`coachingOverlayViewWillActivate(_:)`](arcoachingoverlayviewdelegate/coachingoverlayviewwillactivate(_:).md) to determine whether coaching is in progress. Coordinate your actions to help the user focus on these instructions, for example, by hiding any UI that’s not necessary while the session reinitializes.

##### Relocalizing After an Interruption

If relocalization is enabled (see [`sessionShouldAttemptRelocalization(_:)`](arsessionobserver/sessionshouldattemptrelocalization(_:).md)), ARKit attempts to restore your session if any interruptions degrade your app’s tracking state. In this event, the coaching overlay presents itself and gives the user instructions to assist ARKit with relocalizing.

![User instruction to return to the user’s previous location so ARKit can restore the session. ](/images/com.apple.arkit/media-3394488@2x.png)

During this time, the coaching overlay includes a button that lets the user indicate they’d like to start over rather than restore the session.

![Button that enables the user to indicate they’d like to start over rather than restore the session.](/images/com.apple.arkit/media-3394474@2x.png)

ARKit notifies you when the user presses Start Over by calling your delegate’s [`coachingOverlayViewDidRequestSessionReset(_:)`](arcoachingoverlayviewdelegate/coachingoverlayviewdidrequestsessionreset(_:).md) function. Implement this callback if your app requires any custom actions to restart the AR experience.

```swift
func coachingOverlayViewDidRequestSessionReset(_ coachingOverlayView: ARCoachingOverlayView) {    

    // Reset the session.
    let configuration = ARWorldTrackingConfiguration()
    configuration.planeDetection = [.horizontal, .vertical]
    session.run(configuration, options: [.resetTracking])

    // Custom actions to restart the AR experience. 
    // ...
}
```

If you do not implement [`coachingOverlayViewDidRequestSessionReset(_:)`](arcoachingoverlayviewdelegate/coachingoverlayviewdidrequestsessionreset(_:).md), the coaching overlay responds to the Start Over button by resetting tracking, which also removes any existing anchors.

For more information about relocalization, see [`Managing Session Life Cycle and Tracking Quality`](managing-session-life-cycle-and-tracking-quality.md).

## Topics

### Delegating Events
- [var delegate: (any ARCoachingOverlayViewDelegate)?](arcoachingoverlayview/delegate.md)
  An object you supply that implements coaching event callbacks.
- [protocol ARCoachingOverlayViewDelegate](arcoachingoverlayviewdelegate.md)
  A set of callbacks you implement to be notified of coaching events.
### Defining a Goal
- [var goal: ARCoachingOverlayView.Goal](arcoachingoverlayview/goal-swift.property.md)
  A field that indicates your app’s tracking requirements.
- [ARCoachingOverlayView.Goal](arcoachingoverlayview/goal-swift.enum.md)
  The options that specify your app’s tracking requirements.
### Activating the View
- [var activatesAutomatically: Bool](arcoachingoverlayview/activatesautomatically.md)
  A flag that indicates whether the coaching view activates automatically, depending on the current session state.
- [var isActive: Bool](arcoachingoverlayview/isactive.md)
  A flag that indicates whether coaching is in progress.
- [func setActive(Bool, animated: Bool)](arcoachingoverlayview/setactive(_:animated:).md)
  Controls whether coaching is in progress.
### Providing the Session
- [var session: ARSession?](arcoachingoverlayview/session.md)
  The session this view uses to provide coaching.
- [var sessionProvider: (any ARSessionProviding)?](arcoachingoverlayview/sessionprovider.md)
  An object you designate that provides the current session.

## Relationships

### Inherits From
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [struct RealityView](../realitykit/realityview.md)
  A view that contains RealityKit content.
- [class ARView](../realitykit/arview.md)
  A view that enables you to display an AR experience with RealityKit.
- [class ARSCNView](arscnview.md)
  A view that blends virtual 3D content from SceneKit into your augmented reality experience.
- [class ARSKView](arskview.md)
  A view that blends virtual 2D content from SpriteKit into the 3D space of an augmented reality experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview)*