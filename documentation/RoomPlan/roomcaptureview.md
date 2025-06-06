# RoomCaptureView

**Framework**: RoomPlan  
**Kind**: class

A view that enables the user to scan their room with the device’s camera.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

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

See [`Create a 3D model of an interior room by guiding the user through an AR experience`](https://developer.apple.comhttps://developer.apple.com/documentation/roomplan/create_a_3d_model_of_an_interior_room_by_guiding_the_user_through_an_ar_experience) for a sample code project that demonstrates `RoomCaptureView`.

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
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [protocol RoomCaptureViewDelegate](roomcaptureviewdelegate.md)
  A specification to post-process the results of a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview)*