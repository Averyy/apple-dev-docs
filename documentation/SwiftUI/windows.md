# Windows

**Framework**: SwiftUI

Display user interface content in a window or a collection of windows.

#### Overview

The most common way to present a view hierarchy in your app’s interface is with a [`WindowGroup`](windowgroup.md), which produces a platform-specific behavior and appearance.

![None](https://docs-assets.developer.apple.com/published/9522b0ac981c7a46c7a0319092d0212b/windows-hero%402x.png)

On platforms that support it, people can open multiple windows from the group simultaneously. Each window relies on the same root view definition, but retains its own view state. On some platforms, you can also supplement your app’s user interface with a single-instance window using the [`Window`](window.md) scene type.

Configure windows using scene modifiers that you add to the window declaration, like [`windowStyle(_:)`](scene/windowstyle(_:).md) or [`defaultPosition(_:)`](scene/defaultposition(_:).md). You can also indicate how to configure new windows that you present from a view hierarchy by adding the [`presentedWindowStyle(_:)`](view/presentedwindowstyle(_:).md) view modifier to a view in the hierarchy.

For design guidance, see [`Windows`](https://developer.apple.com/design/Human-Interface-Guidelines/windows) in the Human Interface Guidelines.

## Topics

### Essentials
- [Customizing window styles and state-restoration behavior in macOS](customizing-window-styles-and-state-restoration-behavior-in-macos.md)
  Configure how your app’s windows look and function in macOS to provide an engaging and more coherent experience.
- [Bringing multiple windows to your SwiftUI app](bringing_multiple_windows_to_your_swiftui_app.md)
  Compose rich views by reacting to state changes and customize your app’s scene presentation and behavior on iPadOS and macOS.
### Creating windows
- [struct WindowGroup](windowgroup.md)
  A scene that presents a group of identically structured windows.
- [struct Window](window.md)
  A scene that presents its content in a single, unique window.
- [struct UtilityWindow](utilitywindow.md)
  A specialized window scene that provides secondary utility to the content of the main scenes of an application.
- [protocol WindowStyle](windowstyle.md)
  A specification for the appearance and interaction of a window.
- [func windowStyle<S>(S) -> some Scene](scene/windowstyle(_:).md)
  Sets the style for windows created by this scene.
### Styling the associated toolbar
- [func windowToolbarStyle<S>(S) -> some Scene](scene/windowtoolbarstyle(_:).md)
  Sets the style for the toolbar defined within this scene.
- [func windowToolbarLabelStyle(Binding<ToolbarLabelStyle>) -> some Scene](scene/windowtoolbarlabelstyle(_:).md)
  Sets the label style of items in a toolbar and enables user customization.
- [func windowToolbarLabelStyle(fixed: ToolbarLabelStyle) -> some Scene](scene/windowtoolbarlabelstyle(fixed:).md)
  Sets the label style of items in a toolbar.
- [protocol WindowToolbarStyle](windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.
### Opening windows
- [Presenting windows and spaces](../visionOS/presenting-windows-and-spaces.md)
  Open and close the scenes that make up your app’s interface.
- [var supportsMultipleWindows: Bool](environmentvalues/supportsmultiplewindows.md)
  A Boolean value that indicates whether the current platform supports opening multiple windows.
- [var openWindow: OpenWindowAction](environmentvalues/openwindow.md)
  A window presentation action stored in a view’s environment.
- [struct OpenWindowAction](openwindowaction.md)
  An action that presents a window.
- [struct PushWindowAction](pushwindowaction.md)
  An action that opens the requested window in place of the window the action is called from.
### Closing windows
- [var dismissWindow: DismissWindowAction](environmentvalues/dismisswindow.md)
  A window dismissal action stored in a view’s environment.
- [struct DismissWindowAction](dismisswindowaction.md)
  An action that dismisses a window associated to a particular scene.
- [var dismiss: DismissAction](environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [struct DismissAction](dismissaction.md)
  An action that dismisses a presentation.
- [struct DismissBehavior](dismissbehavior.md)
  Programmatic window dismissal behaviors.
### Sizing a window
- [Positioning and sizing windows](../visionOS/positioning-and-sizing-windows.md)
  Influence the initial geometry of windows that your app presents.
- [func defaultSize(_:)](scene/defaultsize(_:).md)
  Sets a default size for a window.
- [func defaultSize(width: CGFloat, height: CGFloat) -> some Scene](scene/defaultsize(width:height:).md)
  Sets a default width and height for a window.
- [func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some Scene](scene/defaultsize(width:height:depth:).md)
  Sets a default size for a volumetric window.
- [func defaultSize(Size3D, in: UnitLength) -> some Scene](scene/defaultsize(_:in:).md)
  Sets a default size for a volumetric window.
- [func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat, in: UnitLength) -> some Scene](scene/defaultsize(width:height:depth:in:).md)
  Sets a default size for a volumetric window.
- [func windowResizability(WindowResizability) -> some Scene](scene/windowresizability(_:).md)
  Sets the kind of resizability to use for a window.
- [struct WindowResizability](windowresizability.md)
  The resizability of a window.
- [func windowIdealSize(WindowIdealSize) -> some Scene](scene/windowidealsize(_:).md)
  Specifies how windows derived form this scene should determine their size when zooming.
- [struct WindowIdealSize](windowidealsize.md)
  A type which defines the size a window should use when zooming.
### Positioning a window
- [func defaultPosition(UnitPoint) -> some Scene](scene/defaultposition(_:).md)
  Sets a default position for a window.
- [struct WindowLevel](windowlevel.md)
  The level of a window.
- [func windowLevel(WindowLevel) -> some Scene](scene/windowlevel(_:).md)
  Sets the window level of this scene.
- [struct WindowLayoutRoot](windowlayoutroot.md)
  A proxy which represents the root contents of a window.
- [struct WindowPlacement](windowplacement.md)
  A type which represents a preferred size and position for a window.
- [func defaultWindowPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/defaultwindowplacement(_:).md)
  Defines a function used for determining the default placement of windows.
- [func windowIdealPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/windowidealplacement(_:).md)
  Provides a function which determines a placement to use when windows of a scene zoom.
- [struct WindowPlacementContext](windowplacementcontext.md)
  A type which represents contextual information used for sizing and positioning windows.
- [struct WindowProxy](windowproxy.md)
  The proxy for an open window in the app.
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.
### Configuring window visibility
- [struct WindowVisibilityToggle](windowvisibilitytoggle.md)
  A specialized button for toggling the visibility of a window.
- [func defaultLaunchBehavior(SceneLaunchBehavior) -> some Scene](scene/defaultlaunchbehavior(_:).md)
  Sets the default launch behavior for this scene.
- [func restorationBehavior(SceneRestorationBehavior) -> some Scene](scene/restorationbehavior(_:).md)
  Sets the restoration behavior for this scene.
- [struct SceneLaunchBehavior](scenelaunchbehavior.md)
  The launch behavior for a scene.
- [struct SceneRestorationBehavior](scenerestorationbehavior.md)
  The restoration behavior for a scene.
- [func persistentSystemOverlays(Visibility) -> some Scene](scene/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](view/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [struct WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md)
  The visibility of the window toolbar with respect to full screen mode.
### Managing window behavior
- [struct WindowManagerRole](windowmanagerrole.md)
  Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [func windowManagerRole(WindowManagerRole) -> some Scene](scene/windowmanagerrole(_:).md)
  Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [struct WindowInteractionBehavior](windowinteractionbehavior.md)
  Options for enabling and disabling window interaction behaviors.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](view/windowdismissbehavior(_:).md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](view/windowfullscreenbehavior(_:).md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](view/windowminimizebehavior(_:).md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](view/windowresizebehavior(_:).md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowBackgroundDragBehavior(WindowInteractionBehavior) -> some Scene](scene/windowbackgrounddragbehavior(_:).md)
  Configures the behavior of dragging a window by its background.
### Interacting with volumes
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](view/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](view/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [struct VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy.md)
  A type describing when the action provided to [`onVolumeViewpointChange(updateStrategy:initial:_:)`](view/onvolumeviewpointchange(updatestrategy:initial:_:).md) should be called.
- [struct Viewpoint3D](viewpoint3d.md)
  A type describing what direction something is being viewed from.
- [enum SquareAzimuth](squareazimuth.md)
  A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [struct WorldAlignmentBehavior](worldalignmentbehavior.md)
  A type representing the world alignment behavior for a scene.
- [func volumeWorldAlignment(WorldAlignmentBehavior) -> some Scene](scene/volumeworldalignment(_:).md)
  Specifies how a volume should be aligned when moved in the world.
- [struct WorldScalingBehavior](worldscalingbehavior.md)
  Specifies the scaling behavior a window should have within the world.
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](scene/defaultworldscaling(_:).md)
  Specify the world scaling behavior for the window.
- [struct WorldScalingCompensation](worldscalingcompensation.md)
  Indicates whether returned metrics will take dynamic scaling into account.
- [var worldTrackingLimitations: Set<WorldTrackingLimitation>](environmentvalues/worldtrackinglimitations.md)
  The current limitations of the device tracking the user’s surroundings.
- [struct WorldTrackingLimitation](worldtrackinglimitation.md)
  A structure to represent limitations of tracking the user’s surroundings.
- [struct SurfaceSnappingInfo](surfacesnappinginfo.md)
  A type representing information about the window scenes snap state.
### Deprecated Types
- [enum ControlActiveState](controlactivestate.md)
  The active appearance expected of controls in a window.

## See Also

- [App organization](app-organization.md)
  Define the entry point and top-level structure of your app.
- [Scenes](scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](documents.md)
  Enable people to open and manage documents.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](search.md)
  Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windows)*