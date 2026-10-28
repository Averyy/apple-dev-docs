# RoomCaptureView

**Framework**: RoomPlan  
**Kind**: class  
**Role**: Class

A view that enables the user to scan their room with the device’s camera.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class RoomCaptureView
```

## Mentions

- [Scanning the rooms of a single structure](./scanning-the-rooms-of-a-single-structure.md)

## Overview

This class provides your app with a view that manages the scan process from start to finish, including:

- A camera feed that users look through to see their room in AR.
- Real-time graphic overlays that display on top of physical structures in the room to convey scanning progress.
- User instructions that explain how to position the device, if the framework requires a specific kind of device movement or perspective to complete the capture.

When the app determines that the current scan is complete, the view displays a small-scale version of the scanned room for the user to approve.

Alternatively, your app can display custom graphics during the scanning process by creating and using a scan session object ([`RoomCaptureSession`](./roomcapturesession.md)) directly.

See [Create a 3D model of an interior room by guiding the user through an AR experience](./create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience.md) for a sample code project that demonstrates `RoomCaptureView`.

## Topics

### Creating a room-capture view
- [init(frame: CGRect, arSession: ARSession)](./roomcaptureview/init%28frame,arsession%29.md)
  Creates a room-capture view with the given AR session.
- [init(frame: CGRect)](./roomcaptureview/init%28frame%29.md)
  Creates a view that sizes to the specified frame.
- [init?(coder: NSCoder)](./roomcaptureview/init%28coder%29.md)
  Creates a view by deserializing from the specified coder.
### Reacting to scan events
- [var captureSession: RoomCaptureSession!](./roomcaptureview/capturesession.md)
  An object that notifies a delegate of particular events in the room-scanning life cycle.
- [var delegate: (any RoomCaptureViewDelegate)?](./roomcaptureview/delegate.md)
  An object that determines whether to post-process the results of a scan.
### Displaying scan progress
- [var isModelEnabled: Bool](./roomcaptureview/ismodelenabled.md)
  A Boolean value that determines whether the view displays a miniature rendering of the scanned room at the bottom of its bounds.
### Accessing view features
- [var subviews: [UIView]](./roomcaptureview/subviews.md)
  An array that contains the view’s subviews.
- [func layoutSubviews()](./roomcaptureview/layoutsubviews%28%29.md)
  Instructs the view’s subviews to position within the view.
- [func encode(with: NSCoder)](./roomcaptureview/encode%28with%29.md)
  Serializes the view to the specified coder.
- [func traitCollectionDidChange(UITraitCollection?)](./roomcaptureview/traitcollectiondidchange%28_%29.md)
  Notifies the view when the device orientation changes.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### User Interface
- [protocol RoomCaptureViewDelegate](./roomcaptureviewdelegate.md)
  A specification to post-process the results of a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview)*