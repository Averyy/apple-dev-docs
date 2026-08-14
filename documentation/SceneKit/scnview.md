# SCNView

**Framework**: SceneKit  
**Kind**: class

A view for displaying 3D SceneKit content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNView
```

#### Overview

In macOS, [`SCNView`](scnview.md) is a subclass of [`NSView`](https://developer.apple.com/documentation/appkit/nsview). In iOS and tvOS, [`SCNView`](scnview.md) is a subclass of [`UIView`](https://developer.apple.com/documentation/uikit/uiview). As part of either operating system’s view hierarchy, an [`SCNView`](scnview.md) object provides a place for SceneKit content in your app’s user interface. You can create a SceneKit view by using its [`init(frame:options:)`](scnview/init(frame:options:).md) method or by adding it to a nib file or storyboard.  To provide content for a SceneKit view, assign an [`SCNScene`](scnscene.md) object to its [`scene`](scnview/scene.md) property.

For additional important methods and properties for working with SceneKit views, see the [`SCNSceneRenderer`](scnscenerenderer.md) protocol. (You can also render SceneKit content into an arbitrary Metal command queue or OpenGL context using the [`SCNRenderer`](scnrenderer.md) class, or into a Core Animation layer on macOS using the [`SCNLayer`](scnlayer.md) class. The [`SCNSceneRenderer`](scnscenerenderer.md) protocol defines functionality common to all three SceneKit rendering classes.)

## Topics

### Initializing a SceneKit View
- [init(frame: CGRect, options: [String : Any]?)](scnview/init(frame:options:).md)
  Initializes and returns a newly allocated SceneKit view object with the specified frame rectangle and options.
- [SCNView.Option](scnview/option.md)
  Dictionary keys specifying initialization options, used when initializing a SceneKit view.
### Specifying a Scene
- [var scene: SCNScene?](scnview/scene.md)
  The scene to be displayed in the view.
### Configuring a View
- [var backgroundColor: NSColor](scnview/backgroundcolor.md)
  The background color of the view.
- [var preferredFramesPerSecond: Int](scnview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var rendersContinuously: Bool](scnview/renderscontinuously.md)
  A Boolean value that determines whether the view always renders at its preferred frame rate or only when its visible content changes.
- [var antialiasingMode: SCNAntialiasingMode](scnview/antialiasingmode.md)
  The antialiasing mode used for rendering the view’s scene.
- [enum SCNAntialiasingMode](scnantialiasingmode.md)
  Modes for antialiased rendering of the view’s scene, used by the [`SCNView`](scnview.md) property.
### Managing Camera Controls
- [var allowsCameraControl: Bool](scnview/allowscameracontrol.md)
  A Boolean value that determines whether the user can manipulate the current point of view that is used to render the scene.
- [var cameraControlConfiguration: any SCNCameraControlConfiguration](scnview/cameracontrolconfiguration.md)
  The current configuration for the camera controller’s event-handling behavior.
- [protocol SCNCameraControlConfiguration](scncameracontrolconfiguration.md)
  Properties affecting the behavior of a camera controller.
- [var defaultCameraController: SCNCameraController](scnview/defaultcameracontroller.md)
- [class SCNCameraController](scncameracontroller.md)
### Playing Action and Animation in a View’s Scene
- [func pause(Any?)](scnview/pause(_:).md)
  Pauses playback of the view’s scene.
- [func play(Any?)](scnview/play(_:).md)
  Resumes playback of the view’s scene.
- [func stop(Any?)](scnview/stop(_:).md)
  Stops playback of the view’s scene and resets the scene time to its start time.
### Capturing a View Snapshot
- [func snapshot() -> UIImage](scnview/snapshot.md)
  Renders the view’s scene into a new image object.
### Working with a View’s OpenGL ES Context
- [var eaglContext: EAGLContext?](scnview/eaglcontext.md)
  The OpenGL ES context that the view uses to render its contents.
### Working with a View’s OpenGL Context
- [var openGLContext: NSOpenGLContext?](scnview/openglcontext.md)
  The OpenGL context that the view uses to render its contents.
- [var pixelFormat: NSOpenGLPixelFormat?](scnview/pixelformat.md)
  The view’s OpenGL pixel format.
### Instance Properties
- [var drawableResizesAsynchronously: Bool](scnview/drawableresizesasynchronously.md)

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
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
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [SCNSceneRenderer](scnscenerenderer.md)
- [SCNTechniqueSupport](scntechniquesupport.md)
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

- [class SCNScene](scnscene.md)
  A container for the node hierarchy and global properties that together form a displayable 3D scene.
- [struct SceneView](sceneview.md)
  A SwiftUI view for displaying 3D SceneKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview)*