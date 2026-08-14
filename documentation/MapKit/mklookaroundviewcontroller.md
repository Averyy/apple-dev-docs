# MKLookAroundViewController

**Framework**: MapKit  
**Kind**: class

A class that manages the presentation and display of a LookAround view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MKLookAroundViewController
```

## Topics

### Creating a LookAround controller
- [init?(coder: NSCoder)](mklookaroundviewcontroller/init(coder:).md)
  Creates a new LookAround view controller object from a coder object provided by a storyboard or nib file.
- [init(nibName: String?, bundle: Bundle?)](mklookaroundviewcontroller/init(nibname:bundle:).md)
  Creates a new LookAround view controller from the specified nib and bundle.
- [init(scene: MKLookAroundScene)](mklookaroundviewcontroller/init(scene:).md)
  Creates a new LookAround view controller with the specified scene.
### Customizing the LookAround display
- [var isNavigationEnabled: Bool](mklookaroundviewcontroller/isnavigationenabled.md)
  A Boolean value that indicates whether the map’s navigation controls are visible.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mklookaroundviewcontroller/pointofinterestfilter.md)
  The filter used to determine the points of interest shown on the map.
- [var showsRoadLabels: Bool](mklookaroundviewcontroller/showsroadlabels.md)
  A Boolean value that indicates whether the map display road labels.
- [var badgePosition: MKLookAroundBadgePosition](mklookaroundviewcontroller/badgeposition.md)
  A value that indicates the badge’s position on the LookAround view.
- [enum MKLookAroundBadgePosition](mklookaroundbadgeposition.md)
  Constants that control the position of badges on LookAround views.
### Interacting with the controller
- [var delegate: (any MKLookAroundViewControllerDelegate)?](mklookaroundviewcontroller/delegate.md)
  An object you provide to receive events related to the user’s interaction with the LookAround view controller.
- [protocol MKLookAroundViewControllerDelegate](mklookaroundviewcontrollerdelegate.md)
  Methods you implement to respond to changes in the LookAround view controller.
### Accessing the scene
- [var scene: MKLookAroundScene?](mklookaroundviewcontroller/scene.md)
  The LookAround scene.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class MKLookAroundScene](mklookaroundscene.md)
  A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [class MKLookAroundSceneRequest](mklookaroundscenerequest.md)
  A class you use to request a LookAround scene at the location you specify.
- [class MKLookAroundSnapshotter](mklookaroundsnapshotter.md)
  A utility class that you use to create a static image from a LookAround scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontroller)*