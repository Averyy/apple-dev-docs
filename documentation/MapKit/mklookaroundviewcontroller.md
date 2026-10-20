# MKLookAroundViewController

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface MKLookAroundViewController : UIViewController
```

*macOS*

```objc
@interface MKLookAroundViewController : NSViewController
```

## Topics

### Creating a LookAround controller
- [init?(coder: NSCoder)](./mklookaroundviewcontroller/init%28coder%29.md)
  Creates a new LookAround view controller object from a coder object provided by a storyboard or nib file.
- [init(nibName: String?, bundle: Bundle?)](./mklookaroundviewcontroller/init%28nibname,bundle%29.md)
  Creates a new LookAround view controller from the specified nib and bundle.
- [init(scene: MKLookAroundScene)](./mklookaroundviewcontroller/init%28scene%29.md)
  Creates a new LookAround view controller with the specified scene.
### Customizing the LookAround display
- [var isNavigationEnabled: Bool](./mklookaroundviewcontroller/isnavigationenabled.md)
  A Boolean value that indicates whether the map’s navigation controls are visible.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./mklookaroundviewcontroller/pointofinterestfilter.md)
  The filter used to determine the points of interest shown on the map.
- [var showsRoadLabels: Bool](./mklookaroundviewcontroller/showsroadlabels.md)
  A Boolean value that indicates whether the map display road labels.
- [var badgePosition: MKLookAroundBadgePosition](./mklookaroundviewcontroller/badgeposition.md)
  A value that indicates the badge’s position on the LookAround view.
- [enum MKLookAroundBadgePosition](./mklookaroundbadgeposition.md)
  Constants that control the position of badges on LookAround views.
### Interacting with the controller
- [var delegate: (any MKLookAroundViewControllerDelegate)?](./mklookaroundviewcontroller/delegate.md)
  An object you provide to receive events related to the user’s interaction with the LookAround view controller.
- [protocol MKLookAroundViewControllerDelegate](./mklookaroundviewcontrollerdelegate.md)
  Methods you implement to respond to changes in the LookAround view controller.
### Accessing the scene
- [var scene: MKLookAroundScene?](./mklookaroundviewcontroller/scene.md)
  The LookAround scene.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Exploring at street level
- [class MKLookAroundScene](./mklookaroundscene.md)
  A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [class MKLookAroundSceneRequest](./mklookaroundscenerequest.md)
  A class you use to request a LookAround scene at the location you specify.
- [class MKLookAroundSnapshotter](./mklookaroundsnapshotter.md)
  A utility class that you use to create a static image from a LookAround scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontroller)*