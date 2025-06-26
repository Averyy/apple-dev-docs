# Scene

**Framework**: SwiftUI  
**Kind**: protocol

A part of an app’s user interface with a life cycle managed by the system.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol Scene
```

## Mentions

- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)
- [Building and customizing the menu bar with SwiftUI](building-and-customizing-the-menu-bar-with-swiftui.md)

#### Overview

You create an [`App`](app.md) by combining one or more instances that conform to the `Scene` protocol in the app’s [`body`](app/body-swift.property.md). You can use the built-in scenes that SwiftUI provides, like [`WindowGroup`](windowgroup.md), along with custom scenes that you compose from other scenes. To create a custom scene, declare a type that conforms to the `Scene` protocol. Implement the required [`body`](scene/body-swift.property.md) computed property and provide the content for your custom scene:

```swift
struct MyScene: Scene {
    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
    }
}
```

A scene acts as a container for a view hierarchy that you want to display to the user. The system decides when and how to present the view hierarchy in the user interface in a way that’s platform-appropriate and dependent on the current state of the app. For example, for the window group shown above, the system lets the user create or remove windows that contain `MyRootView` on platforms like macOS and iPadOS. On other platforms, the same view hierarchy might consume the entire display when active.

Read the [`scenePhase`](environmentvalues/scenephase.md) environment value from within a scene or one of its views to check whether a scene is active or in some other state. You can create a property that contains the scene phase, which is one of the values in the [`ScenePhase`](scenephase.md) enumeration, using the [`Environment`](environment.md) attribute:

```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase

    // ...
}
```

The `Scene` protocol provides scene modifiers, defined as protocol methods with default implementations, that you use to configure a scene. For example, you can use the [`onChange(of:perform:)`](scene/onchange(of:perform:).md) modifier to trigger an action when a value changes. The following code empties a cache when all of the scenes in the window group have moved to the background:

```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var cache = DataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
        .onChange(of: scenePhase) { newScenePhase in
            if newScenePhase == .background {
                cache.empty()
            }
        }
    }
}
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Creating a scene
- [var body: Self.Body](scene/body-swift.property.md)
  The content and behavior of the scene.
- [associatedtype Body : Scene](scene/body-swift.associatedtype.md)
  The type of scene that represents the body of this scene.
### Watching for changes
- [func onChange(of:initial:_:)](scene/onchange(of:initial:_:).md)
  Adds an action to perform when the given value changes.
- [func handlesExternalEvents(matching: Set<String>) -> some Scene](scene/handlesexternalevents(matching:).md)
  Specifies the external events for which SwiftUI opens a new instance of the modified scene.
### Creating background tasks
- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some Scene](scene/backgroundtask(_:action:).md)
  Runs the specified action when the system provides a background task.
### Managing app storage
- [func defaultAppStorage(UserDefaults) -> some Scene](scene/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the scene and its view content.
### Setting commands
- [func commands<Content>(content: () -> Content) -> some Scene](scene/commands(content:).md)
  Adds commands to the scene.
- [func commandsRemoved() -> some Scene](scene/commandsremoved.md)
  Removes all commands defined by the modified scene.
- [func commandsReplaced<Content>(content: () -> Content) -> some Scene](scene/commandsreplaced(content:).md)
  Replaces all commands defined by the modified scene with the commands from the builder.
- [func keyboardShortcut(KeyboardShortcut?) -> some Scene](scene/keyboardshortcut(_:).md)
  Defines a keyboard shortcut for opening new scene windows.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some Scene](scene/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut for opening new scene windows.
### Sizing and positioning the scene
- [func defaultPosition(UnitPoint) -> some Scene](scene/defaultposition(_:).md)
  Sets a default position for a window.
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
- [func defaultWindowPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/defaultwindowplacement(_:).md)
  Defines a function used for determining the default placement of windows.
- [func windowResizability(WindowResizability) -> some Scene](scene/windowresizability(_:).md)
  Sets the kind of resizability to use for a window.
- [func windowIdealSize(WindowIdealSize) -> some Scene](scene/windowidealsize(_:).md)
  Specifies how windows derived form this scene should determine their size when zooming.
- [func windowIdealPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/windowidealplacement(_:).md)
  Provides a function which determines a placement to use when windows of a scene zoom.
- [func windowManagerRole(WindowManagerRole) -> some Scene](scene/windowmanagerrole(_:).md)
  Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
### Interacting with volumes
- [func volumeWorldAlignment(WorldAlignmentBehavior) -> some Scene](scene/volumeworldalignment(_:).md)
  Specifies how a volume should be aligned when moved in the world.
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](scene/defaultworldscaling(_:).md)
  Specify the world scaling behavior for the window.
### Configuring scene visibility
- [func defaultLaunchBehavior(SceneLaunchBehavior) -> some Scene](scene/defaultlaunchbehavior(_:).md)
  Sets the default launch behavior for this scene.
- [func restorationBehavior(SceneRestorationBehavior) -> some Scene](scene/restorationbehavior(_:).md)
  Sets the restoration behavior for this scene.
- [func persistentSystemOverlays(Visibility) -> some Scene](scene/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
### Styling the scene
- [func immersionStyle(selection: Binding<any ImmersionStyle>, in: any ImmersionStyle...) -> some Scene](scene/immersionstyle(selection:in:).md)
  Sets the style for an immersive space.
- [func upperLimbVisibility(Visibility) -> some Scene](scene/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](immersivespace.md) scene is presented.
- [func windowStyle<S>(S) -> some Scene](scene/windowstyle(_:).md)
  Sets the style for windows created by this scene.
- [func windowLevel(WindowLevel) -> some Scene](scene/windowlevel(_:).md)
  Sets the window level of this scene.
- [func windowToolbarStyle<S>(S) -> some Scene](scene/windowtoolbarstyle(_:).md)
  Sets the style for the toolbar defined within this scene.
- [func windowToolbarLabelStyle(Binding<ToolbarLabelStyle>) -> some Scene](scene/windowtoolbarlabelstyle(_:).md)
  Sets the label style of items in a toolbar and enables user customization.
- [func windowToolbarLabelStyle(fixed: ToolbarLabelStyle) -> some Scene](scene/windowtoolbarlabelstyle(fixed:).md)
  Sets the label style of items in a toolbar.
### Configuring a data model
- [func modelContext(ModelContext) -> some Scene](scene/modelcontext(_:).md)
  Sets the model context in this scene’s environment.
- [func modelContainer(ModelContainer) -> some Scene](scene/modelcontainer(_:).md)
  Sets the model container and associated model context in this scene’s environment.
- [func modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](scene/modelcontainer(for:inmemory:isautosaveenabled:isundoenabled:onsetup:).md)
  Sets the model container in this scene for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this scene’s environment.
### Managing the environment
- [func environment<T>(T?) -> some Scene](scene/environment(_:).md)
  Places an observable object in the scene’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene](scene/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func environmentObject<T>(T) -> some Scene](scene/environmentobject(_:).md)
  Supplies an `ObservableObject` to a view subhierarchy.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some Scene](scene/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
### Interacting with dialogs
- [func dialogIcon(Image?) -> some Scene](scene/dialogicon(_:).md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some Scene](scene/dialogseverity(_:).md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](scene/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogSuppressionToggle(_:isSuppressed:)](scene/dialogsuppressiontoggle(_:issuppressed:).md)
  Enables user suppression of an alert with a custom suppression message.
### Supporting drag behavior
- [func windowBackgroundDragBehavior(WindowInteractionBehavior) -> some Scene](scene/windowbackgrounddragbehavior(_:).md)
  Configures the behavior of dragging a window by its background.
### Deprecated symbols
- [func onChange<V>(of: V, perform: (V) -> Void) -> some Scene](scene/onchange(of:perform:).md)
  Adds an action to perform when the given value changes.
### Instance Methods
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some Scene](scene/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentGroupLaunchScene` actions that accept a list of selected files as their parameter.
- [func immersiveContentBrightness(ImmersiveContentBrightness) -> some Scene](scene/immersivecontentbrightness(_:).md)
  Sets the content brightness of an immersive space.
- [func immersiveEnvironmentBehavior(ImmersiveEnvironmentBehavior) -> some Scene](scene/immersiveenvironmentbehavior(_:).md)
  Sets the immersive environment behavior that should apply when this scene opens.
- [func menuBarExtraStyle<S>(S) -> some Scene](scene/menubarextrastyle(_:).md)
  Sets the style for menu bar extra created by this scene.

## Relationships

### Conforming Types
- [AlertScene](alertscene.md)
- [AssistiveAccess](assistiveaccess.md)
- [DocumentGroup](documentgroup.md)
- [DocumentGroupLaunchScene](documentgrouplaunchscene.md)
- [Group](group.md)
- [ImmersiveSpace](immersivespace.md)
- [MenuBarExtra](menubarextra.md)
- [ModifiedContent](modifiedcontent.md)
- [RemoteImmersiveSpace](remoteimmersivespace.md)
- [Settings](settings.md)
- [UtilityWindow](utilitywindow.md)
- [WKNotificationScene](wknotificationscene.md)
- [Window](window.md)
- [WindowGroup](windowgroup.md)

## See Also

- [struct SceneBuilder](scenebuilder.md)
  A result builder for composing a collection of scenes into a single composite scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene)*