# RoomCaptureView

**Framework**: RoomPlan  
**Kind**: class

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

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Overview

This class provides your app with a view that manages the scan process from start to finish, including:

- A camera feed that users look through to see their room in AR.
- Real-time graphic overlays that display on top of physical structures in the room to convey scanning progress.
- User instructions that explain how to position the device, if the framework requires a specific kind of device movement or perspective to complete the capture.

When the app determines that the current scan is complete, the view displays a small-scale version of the scanned room for the user to approve.

Alternatively, your app can display custom graphics during the scanning process by creating and using a scan session object ([`RoomCaptureSession`](roomcapturesession.md)) directly.

See [`Create a 3D model of an interior room by guiding the user through an AR experience`](create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience.md) for a sample code project that demonstrates `RoomCaptureView`.

## Topics

### Creating a room-capture view
- [init(frame: CGRect, arSession: ARSession)](roomcaptureview/init(frame:arsession:).md)
  Creates a room-capture view with the given AR session.
- [init(frame: CGRect)](roomcaptureview/init(frame:).md)
  Creates a view that sizes to the specified frame.
- [init?(coder: NSCoder)](roomcaptureview/init(coder:).md)
  Creates a view by deserializing from the specified coder.
### Reacting to scan events
- [var captureSession: RoomCaptureSession!](roomcaptureview/capturesession.md)
  An object that notifies a delegate of particular events in the room-scanning life cycle.
- [var delegate: (any RoomCaptureViewDelegate)?](roomcaptureview/delegate.md)
  An object that determines whether to post-process the results of a scan.
### Displaying scan progress
- [var isModelEnabled: Bool](roomcaptureview/ismodelenabled.md)
  A Boolean value that determines whether the view displays a miniature rendering of the scanned room at the bottom of its bounds.
### Accessing view features
- [var subviews: [UIView]](roomcaptureview/subviews.md)
  An array that contains the view’s subviews.
- [func layoutSubviews()](roomcaptureview/layoutsubviews.md)
  Instructs the view’s subviews to position within the view.
- [func encode(with: NSCoder)](roomcaptureview/encode(with:).md)
  Serializes the view to the specified coder.
- [func traitCollectionDidChange(UITraitCollection?)](roomcaptureview/traitcollectiondidchange(_:).md)
  Notifies the view when the device orientation changes.

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
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
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

- [protocol RoomCaptureViewDelegate](roomcaptureviewdelegate.md)
  A specification to post-process the results of a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview)*