# Input and event modifiers

**Framework**: SwiftUI

Supply actions for a view to perform in response to user input and system events.

#### Overview

Use input and event modifiers to configure and provide handlers for a wide variety of user inputs or system events. For example, you can detect and control focus, respond to life cycle events like view appearance and disappearance, manage keyboard shortcuts, and much more.

## Topics

### Interactivity
- [func disabled(Bool) -> some View](view/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func interactionActivityTrackingTag(String) -> some View](view/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
### List controls
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](view/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func refreshable(action: () async -> Void) -> some View](view/refreshable(action:).md)
  Marks this view as refreshable.
- [func selectionDisabled(Bool) -> some View](view/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
### Scroll controls
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](view/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](view/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func defaultScrollAnchor(UnitPoint?) -> some View](view/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](view/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](view/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](view/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](view/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](view/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onScrollPhaseChange(_:)](view/onscrollphasechange(_:).md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
### Geometry
- [func onGeometryChange(for:of:action:)](view/ongeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
### Taps and gestures
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](view/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onTapGesture(count:coordinateSpace:perform:)](view/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongTouchGesture(minimumDuration: Double, perform: () -> Void, onTouchingChanged: ((Bool) -> Void)?) -> some View](view/onlongtouchgesture(minimumduration:perform:ontouchingchanged:).md)
  Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [func gesture(some UIGestureRecognizerRepresentable) -> some View](view/gesture(_:).md)
  Attaches a [`UIGestureRecognizerRepresentable`](uigesturerecognizerrepresentable.md) to the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](view/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](view/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, including: GestureMask) -> some View](view/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](view/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](view/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](view/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](view/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func defersSystemGestures(on: Edge.Set) -> some View](view/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](view/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](view/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [func allowsWindowActivationEvents(Bool?) -> some View](view/allowswindowactivationevents(_:).md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
### Keyboard input
- [func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View](view/onkeypress(_:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](view/onkeypress(phases:action:).md)
  Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](view/onkeypress(_:phases:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](view/onkeypress(characters:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](view/onkeypress(keys:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onModifierKeysChanged(mask: EventModifiers, initial: Bool, (EventModifiers, EventModifiers) -> Void) -> some View](view/onmodifierkeyschanged(mask:initial:_:).md)
  Performs an action whenever the user presses or releases a hardware modifier key.
### Keyboard shortcuts
- [func keyboardShortcut(_:)](view/keyboardshortcut(_:).md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](view/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](view/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func modifierKeyAlternate<V>(EventModifiers, () -> V) -> some View](view/modifierkeyalternate(_:_:).md)
  Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.
### Hover
- [func onHover(perform: (Bool) -> Void) -> some View](view/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onContinuousHover(coordinateSpace:perform:)](view/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func hoverEffect(HoverEffect) -> some View](view/hovereffect(_:).md)
  Applies a hover effect to this view.
- [func hoverEffect(_:isEnabled:)](view/hovereffect(_:isenabled:).md)
  Applies a hover effect to this view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](view/hovereffect(_:in:isenabled:).md)
  Applies a hover effect to this view, optionally adding it to a [`HoverEffectGroup`](hovereffectgroup.md).
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](view/hovereffect(in:isenabled:body:).md)
  Applies a hover effect to this view described by the given closure.
- [func hoverEffectGroup() -> some View](view/hovereffectgroup.md)
  Adds an implicit [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](view/hovereffectgroup(_:).md)
  Adds a [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](view/hovereffectgroup(id:in:behavior:).md)
  Adds a [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectDisabled(Bool) -> some View](view/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func defaultHoverEffect(_:)](view/defaulthovereffect(_:).md)
  Sets the default hover effect to use for views within this view.
- [func listRowHoverEffect(HoverEffect?) -> some View](view/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](view/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
### Pointer
- [func pointerVisibility(Visibility) -> some View](view/pointervisibility(_:).md)
  Sets the visibility of the pointer when it’s over the view.
- [func pointerStyle(PointerStyle?) -> some View](view/pointerstyle(_:).md)
  Sets the pointer style to display when the pointer is over the view.
### Focus
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](view/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focused(FocusState<Bool>.Binding) -> some View](view/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focusedValue<T>(T?) -> some View](view/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue(_:_:)](view/focusedvalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func focusedSceneValue<T>(T?) -> some View](view/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue(_:_:)](view/focusedscenevalue(_:_:).md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [func focusedObject(_:)](view/focusedobject(_:).md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [func focusedSceneObject(_:)](view/focusedsceneobject(_:).md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View](view/prefersdefaultfocus(_:in:).md)
  Indicates that the view should receive focus by default for a given namespace.
- [func focusScope(Namespace.ID) -> some View](view/focusscope(_:).md)
  Creates a focus scope that SwiftUI uses to limit default focus preferences.
- [func focusSection() -> some View](view/focussection.md)
  Indicates that the view’s frame and cohort of focusable descendants should be used to guide focus movement.
- [func focusable(Bool) -> some View](view/focusable(_:).md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](view/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [func focusEffectDisabled(Bool) -> some View](view/focuseffectdisabled(_:).md)
  Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](view/defaultfocus(_:_:priority:).md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](view/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](view/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
### Copy and paste
- [func copyable<T>(@autoclosure () -> [T]) -> some View](view/copyable(_:).md)
  Specifies a list of items to copy in response to the system’s Copy command.
- [func cuttable<T>(for: T.Type, action: () -> [T]) -> some View](view/cuttable(for:action:).md)
  Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T]) -> [T]) -> some View](view/pastedestination(for:action:validator:).md)
  Specifies an action that adds validated items to a view in response to the system’s Paste command.
- [func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View](view/oncopycommand(perform:).md)
  Adds an action to perform in response to the system’s Copy command.
- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](view/oncutcommand(perform:).md)
  Adds an action to perform in response to the system’s Cut command.
- [func onPasteCommand(of:perform:)](view/onpastecommand(of:perform:).md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of:validator:perform:)](view/onpastecommand(of:validator:perform:).md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
### Drag and drop
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](view/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](view/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](view/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrop(of:isTargeted:perform:)](view/ondrop(of:istargeted:perform:).md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of:delegate:)](view/ondrop(of:delegate:).md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](view/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func draggable<T>(@autoclosure () -> T) -> some View](view/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](view/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](view/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
### Submission
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](view/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](view/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func submitLabel(SubmitLabel) -> some View](view/submitlabel(_:).md)
  Sets the submit label for this view.
### Movement
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](view/onmovecommand(perform:).md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func moveDisabled(Bool) -> some View](view/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
### Deletion
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](view/ondeletecommand(perform:).md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func deleteDisabled(Bool) -> some View](view/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
### Commands
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](view/pagecommand(value:in:step:).md)
  Steps a value through a range in response to page up or page down commands.
- [func onExitCommand(perform: (() -> Void)?) -> some View](view/onexitcommand(perform:).md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](view/onplaypausecommand(perform:).md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](view/oncommand(_:perform:).md)
  Adds an action to perform in response to the given selector.
### Digital crown
- [func digitalCrownAccessory(Visibility) -> some View](view/digitalcrownaccessory(_:).md)
  Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](view/digitalcrownaccessory(content:).md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](view/digitalcrownrotation(_:from:through:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](view/digitalcrownrotation(_:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](view/digitalcrownrotation(detent:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>) -> some View](view/digitalcrownrotation(_:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](view/digitalcrownrotation(_:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:).md)
  Tracks Digital Crown rotations by updating the specified binding.
### Immersive Spaces
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](view/onimmersionchange(initial:_:).md)
  Performs an action when the immersion state of your app changes.
### Volumes
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](view/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](view/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
### User activities
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](view/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](view/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](view/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](view/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
### View life cycle
- [func onAppear(perform: (() -> Void)?) -> some View](view/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onDisappear(perform: (() -> Void)?) -> some View](view/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func onChange(of:initial:_:)](view/onchange(of:initial:_:).md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func task(priority: TaskPriority, () async -> Void) -> some View](view/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](view/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
### File renaming
- [func renameAction(_:)](view/renameaction(_:).md)
  Sets a closure to run for the rename action.
### URLs
- [func onOpenURL(perform: (URL) -> ()) -> some View](view/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
- [func widgetURL(URL?) -> some View](view/widgeturl(_:).md)
  Sets the URL to open in the containing app when the user clicks the widget.
### Publisher events
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](view/onreceive(_:perform:).md)
  Adds an action to perform when this view detects data emitted by the given publisher.
### Hit testing
- [func allowsHitTesting(Bool) -> some View](view/allowshittesting(_:).md)
  Configures whether this view participates in hit test operations.
### Content shape
- [func contentShape<S>(S, eoFill: Bool) -> some View](view/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](view/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.
### Import and export
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some View](view/exportsitemproviders(_:onexport:).md)
  Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit: ([NSItemProvider]) -> Bool) -> some View](view/exportsitemproviders(_:onexport:onedit:).md)
  Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](view/importsitemproviders(_:onimport:).md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](view/exportabletoservices(_:).md)
  Exports items for consumption by shortcuts, quick actions, and services.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](view/exportabletoservices(_:onedit:).md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.
- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](view/importablefromservices(for:action:).md)
  Enables importing items from services, such as Continuity Camera on macOS.
### App intents
- [func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View](view/shortcutslinkstyle(_:).md)
  Sets the given style for ShortcutsLinks within the view hierarchy
- [func siriTipViewStyle(SiriTipViewStyle) -> some View](view/siritipviewstyle(_:).md)
  Sets the given style for SiriTipView within the view hierarchy
### Camera
- [func onCameraCaptureEvent(isEnabled: Bool, action: (AVCaptureEvent) -> Void) -> some View](view/oncameracaptureevent(isenabled:action:).md)
  Used to register an action triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled: Bool, primaryAction: (AVCaptureEvent) -> Void, secondaryAction: (AVCaptureEvent) -> Void) -> some View](view/oncameracaptureevent(isenabled:primaryaction:secondaryaction:).md)
  Used to register actions triggered by system capture events.
- [func cameraAnchor(isActive: Bool) -> some View](view/cameraanchor(isactive:).md)
  Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.

## See Also

- [Search modifiers](view-search.md)
  Enable people to search for content in your app.
- [Presentation modifiers](view-presentation.md)
  Define additional views for the view to present under specified conditions.
- [State modifiers](view-state.md)
  Access storage and provide child views with configuration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-input-and-events)*