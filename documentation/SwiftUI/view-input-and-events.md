# Input and event modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Supply actions for a view to perform in response to user input and system events.

#### Overview

Use input and event modifiers to configure and provide handlers for a wide variety of user inputs or system events. For example, you can detect and control focus, respond to life cycle events like view appearance and disappearance, manage keyboard shortcuts, and much more.

## Topics

### Interactivity
- [func disabled(Bool) -> some View](./view/disabled%28_%29.md)
  Adds a condition that controls whether someone can interact with this view.
- [func interactionActivityTrackingTag(String) -> some View](./view/interactionactivitytrackingtag%28_%29.md)
  Sets a tag that you use for tracking interactivity.
### List controls
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](./view/swipeactions%28edge,allowsfullswipe,content%29.md)
  Adds custom swipe actions to a row in a list.
- [func refreshable(action: () async -> Void) -> some View](./view/refreshable%28action%29.md)
  Adds an asynchronous handler that can update the data the view displays when a person initiates a request, such as by pulling to refresh.
- [func selectionDisabled(Bool) -> some View](./view/selectiondisabled%28_%29.md)
  Adds a condition that controls whether users can select this view.
### Container controls
- [func swipeActions(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> some View, onPresentationChanged: (Bool) -> Void) -> some View](./view/swipeactions%28edge,allowsfullswipe,content,onpresentationchanged%29.md)
  Adds custom swipe actions to a row in a list or container, notifying you when the actions are revealed or dismissed.
- [func swipeActionsContainer() -> some View](./view/swipeactionscontainer%28%29.md)
  Coordinates swipe action dismissal and mutual exclusion across rows in a container.
### Scroll controls
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](./view/scrollposition%28_,anchor%29.md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](./view/scrollposition%28id,anchor%29.md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func defaultScrollAnchor(UnitPoint?) -> some View](./view/defaultscrollanchor%28_%29.md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](./view/defaultscrollanchor%28_,for%29.md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](./view/scrolltargetbehavior%28_%29.md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](./view/scrolltargetlayout%28isenabled%29.md)
  Configures the outermost layout as a scroll target layout.
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](./view/scrollinputbehavior%28_,for%29.md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](./view/scrolltransition%28_,axis,transition%29.md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](./view/scrolltransition%28topleading,bottomtrailing,axis,transition%29.md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](./view/onscrollgeometrychange%28for,of,action%29.md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](./view/onscrolltargetvisibilitychange%28idtype,threshold,_%29.md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](./view/onscrollvisibilitychange%28threshold,_%29.md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onScrollPhaseChange(_:)](./view/onscrollphasechange%28_%29.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
### Geometry
- [func onGeometryChange(for:of:action:)](./view/ongeometrychange%28for,of,action%29.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange3D(for:of:action:)](./view/ongeometrychange3d%28for,of,action%29.md)
  Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onInteractiveResizeChange((Bool) -> Void) -> some View](./view/oninteractiveresizechange%28_%29.md)
  Adds an action to perform when the enclosing window is being interactively resized.
### Taps and gestures
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](./view/ontapgesture%28count,perform%29.md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol, inputKinds: GestureInputKinds, perform: (CGPoint) -> Void) -> some View](./view/ontapgesture%28count,coordinatespace,inputkinds,perform%29.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](./view/onlongpressgesture%28minimumduration,maximumdistance,perform,onpressingchanged%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, inputKinds: GestureInputKinds, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](./view/onlongpressgesture%28minimumduration,maximumdistance,inputkinds,perform,onpressingchanged%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](./view/onlongpressgesture%28minimumduration,perform,onpressingchanged%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongTouchGesture(minimumDuration: Double, perform: () -> Void, onTouchingChanged: ((Bool) -> Void)?) -> some View](./view/onlongtouchgesture%28minimumduration,perform,ontouchingchanged%29.md)
  Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [func gesture(_:)](./view/gesture%28_%29.md)
  Attaches an [`NSGestureRecognizerRepresentable`](./nsgesturerecognizerrepresentable.md) to the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](./view/gesture%28_,isenabled%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](./view/gesture%28_,name,isenabled%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, including: GestureMask) -> some View](./view/gesture%28_,including%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](./view/highprioritygesture%28_,including%29.md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](./view/highprioritygesture%28_,isenabled%29.md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](./view/highprioritygesture%28_,name,isenabled%29.md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](./view/simultaneousgesture%28_,including%29.md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](./view/simultaneousgesture%28_,isenabled%29.md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](./view/simultaneousgesture%28_,name,isenabled%29.md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func defersSystemGestures(on: Edge.Set) -> some View](./view/deferssystemgestures%28on%29.md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](./view/onpencildoubletap%28perform%29.md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](./view/onpencilsqueeze%28perform%29.md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [func allowsWindowActivationEvents() -> some View](./view/allowswindowactivationevents%28%29.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](./view/allowswindowactivationevents%28_%29.md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
- [func onTapGesture(count:coordinateSpace:perform:)](./view/ontapgesture%28count,coordinatespace,perform%29.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
### Keyboard input
- [func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View](./view/onkeypress%28_,action%29.md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](./view/onkeypress%28phases,action%29.md)
  Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](./view/onkeypress%28_,phases,action%29.md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](./view/onkeypress%28characters,phases,action%29.md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](./view/onkeypress%28keys,phases,action%29.md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onModifierKeysChanged(mask: EventModifiers, initial: Bool, (EventModifiers, EventModifiers) -> Void) -> some View](./view/onmodifierkeyschanged%28mask,initial,_%29.md)
  Performs an action whenever the user presses or releases a hardware modifier key.
### Keyboard shortcuts
- [func keyboardShortcut(_:)](./view/keyboardshortcut%28_%29.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](./view/keyboardshortcut%28_,modifiers%29.md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](./view/keyboardshortcut%28_,modifiers,localization%29.md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func modifierKeyAlternate<V>(EventModifiers, () -> V) -> some View](./view/modifierkeyalternate%28_,_%29.md)
  Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.
### Hand interactions
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](./view/handgestureshortcut%28_,isenabled%29.md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](./view/handpointerbehavior%28_%29.md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func manipulable(coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./view/manipulable%28coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Allows this view to be manipulated using common hand gestures.
- [func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./view/manipulable%28transform,coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [func manipulable(using: Manipulable.GestureState) -> some View](./view/manipulable%28using%29.md)
  Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./view/manipulationgesture%28updating,coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
### Hover
- [func onHover(perform: (Bool) -> Void) -> some View](./view/onhover%28perform%29.md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func hoverEffect(HoverEffect) -> some View](./view/hovereffect%28_%29.md)
  Applies a hover effect to this view.
- [func hoverEffect(_:isEnabled:)](./view/hovereffect%28_,isenabled%29.md)
  Applies a hover effect to this view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](./view/hovereffect%28_,in,isenabled%29.md)
  Applies a hover effect to this view, optionally adding it to a [`HoverEffectGroup`](./hovereffectgroup.md).
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](./view/hovereffect%28in,isenabled,body%29.md)
  Applies a hover effect to this view described by the given closure.
- [func hoverEffectGroup() -> some View](./view/hovereffectgroup%28%29.md)
  Adds an implicit [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](./view/hovereffectgroup%28_%29.md)
  Adds a [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](./view/hovereffectgroup%28id,in,behavior%29.md)
  Adds a [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectDisabled(Bool) -> some View](./view/hovereffectdisabled%28_%29.md)
  Adds a condition that controls whether this view can display hover effects.
- [func defaultHoverEffect(_:)](./view/defaulthovereffect%28_%29.md)
  Sets the default hover effect to use for views within this view.
- [func listRowHoverEffect(HoverEffect?) -> some View](./view/listrowhovereffect%28_%29.md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](./view/listrowhovereffectdisabled%28_%29.md)
  Requests that the containing list row have its hover effect disabled.
- [func onContinuousHover(coordinateSpace:perform:)](./view/oncontinuoushover%28coordinatespace,perform%29.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
### Pointer
- [func pointerVisibility(Visibility) -> some View](./view/pointervisibility%28_%29.md)
  Sets the visibility of the pointer when it’s over the view.
- [func pointerStyle(PointerStyle?) -> some View](./view/pointerstyle%28_%29.md)
  Sets the pointer style to display when the pointer is over the view.
### Focus
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](./view/focused%28_,equals%29.md)
  Modifies this view by binding its focus state to the given state value.
- [func focused(FocusState<Bool>.Binding) -> some View](./view/focused%28_%29.md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focusedValue<T>(T?) -> some View](./view/focusedvalue%28_%29.md)
  Sets the focused value for the given object type.
- [func focusedValue(_:_:)](./view/focusedvalue%28_,_%29.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func focusedSceneValue<T>(T?) -> some View](./view/focusedscenevalue%28_%29.md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue(_:_:)](./view/focusedscenevalue%28_,_%29.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [func focusedObject(_:)](./view/focusedobject%28_%29.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [func focusedSceneObject(_:)](./view/focusedsceneobject%28_%29.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View](./view/prefersdefaultfocus%28_,in%29.md)
  Indicates that the view should receive focus by default for a given namespace.
- [func focusScope(Namespace.ID) -> some View](./view/focusscope%28_%29.md)
  Creates a focus scope that SwiftUI uses to limit default focus preferences.
- [func focusSection() -> some View](./view/focussection%28%29.md)
  Indicates that the view’s frame and cohort of focusable descendants should be used to guide focus movement.
- [func focusable(Bool) -> some View](./view/focusable%28_%29.md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](./view/focusable%28_,interactions%29.md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [func focusEffectDisabled(Bool) -> some View](./view/focuseffectdisabled%28_%29.md)
  Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](./view/defaultfocus%28_,_,priority%29.md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](./view/searchfocused%28_%29.md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](./view/searchfocused%28_,equals%29.md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
### Copy and paste
- [func copyable<T>(@autoclosure () -> [T]) -> some View](./view/copyable%28_%29.md)
  Specifies a list of items to copy in response to the system’s Copy command.
- [func cuttable<T>(for: T.Type, action: () -> [T]) -> some View](./view/cuttable%28for,action%29.md)
  Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T]) -> [T]) -> some View](./view/pastedestination%28for,action,validator%29.md)
  Specifies an action that adds validated items to a view in response to the system’s Paste command.
- [func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View](./view/oncopycommand%28perform%29.md)
  Adds an action to perform in response to the system’s Copy command.
- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](./view/oncutcommand%28perform%29.md)
  Adds an action to perform in response to the system’s Cut command.
- [func onPasteCommand(of:perform:)](./view/onpastecommand%28of,perform%29.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of:validator:perform:)](./view/onpastecommand%28of,validator,perform%29.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
### Drag and drop
- [func dragConfiguration(DragConfiguration) -> some View](./view/dragconfiguration%28_%29.md)
  Configures a drag session.
- [func dragContainer(for:in:_:)](./view/dragcontainer%28for,in,_%29.md)
  A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [func dragContainer(for:itemID:in:_:)](./view/dragcontainer%28for,itemid,in,_%29.md)
  A container with draggable views.
- [func dragContainerSelection<ItemID>(@autoclosure () -> Array<ItemID>, containerNamespace: Namespace.ID?) -> some View](./view/dragcontainerselection%28_,containernamespace%29.md)
  Provides multiple item selection support for drag containers.
- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](./view/dragpreviewsformation%28_%29.md)
  Describes the way dragged previews are visually composed.
- [func draggable<T>(@autoclosure () -> T) -> some View](./view/draggable%28_%29.md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](./view/draggable%28_,preview%29.md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<Item>(Item.Type, containerNamespace: Namespace.ID?, () -> Item?) -> some View](./view/draggable%28_,containernamespace,_%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, containerNamespace: Namespace.ID?, () -> Item?) -> some View](./view/draggable%28_,id,containernamespace,_%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item, ItemID>(Item.Type, id: KeyPath<Item, ItemID>, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](./view/draggable%28_,id,item,containernamespace%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [func draggable<Item>(Item.Type, item: @autoclosure () -> Item?, containerNamespace: Namespace.ID?) -> some View](./view/draggable%28_,item,containernamespace%29.md)
  Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID?) -> some View](./view/draggable%28containeritemid,containernamespace%29.md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](./view/dropconfiguration%28_%29.md)
  Configures a drop session.
- [func dropDestination<T>(for: T.Type, isEnabled: Bool, action: ([T], DropSession) -> Void) -> some View](./view/dropdestination%28for,isenabled,action%29.md)
  Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](./view/droppreviewsformation%28_%29.md)
  Describes the way previews for a drop are composed.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](./view/itemprovider%28_%29.md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](./view/ondrag%28_,preview%29.md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](./view/ondrag%28_%29.md)
  Activates this view as the source of a drag and drop operation.
- [func onDragSessionUpdated((DragSession) -> Void) -> some View](./view/ondragsessionupdated%28_%29.md)
  Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or anther drag modifiers.
- [func onDrop(of:isTargeted:perform:)](./view/ondrop%28of,istargeted,perform%29.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of:delegate:)](./view/ondrop%28of,delegate%29.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDropSessionUpdated((DropSession) -> Void) -> some View](./view/ondropsessionupdated%28_%29.md)
  Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](./view/springloadingbehavior%28_%29.md)
  Sets the spring loading behavior this view.
### Reordering
- [func reorderContainer<Item>(for: Item.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](./view/reordercontainer%28for,isenabled,move%29.md)
  Defines a container of reorderable views.
- [func reorderContainer<Item, CollectionID>(for: Item.Type, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<Item.ID, CollectionID>) -> ()) -> some View](./view/reordercontainer%28for,in,isenabled,move%29.md)
  Defines a container of reorderable views, with a type you specify to identify sections.
- [func reorderContainer<Item, ItemID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, isEnabled: Bool, move: (ReorderDifference<ItemID, ReorderableSingleCollectionIdentifier>) -> ()) -> some View](./view/reordercontainer%28for,itemid,isenabled,move%29.md)
  Defines a container of reorderable views, with a type and keypath you specify to identify items.
- [func reorderContainer<Item, ItemID, CollectionID>(for: Item.Type, itemID: KeyPath<Item, ItemID>, in: CollectionID.Type, isEnabled: Bool, move: (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View](./view/reordercontainer%28for,itemid,in,isenabled,move%29.md)
  Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections.
### Submission
- [func onAssignedDocumentDidSubmit((URL) -> Void) -> some View](./view/onassigneddocumentdidsubmit%28_%29.md)
  Adds an action to perform after submitting an assigned document.
- [func onAssignedDocumentDidWithdraw((URL) -> Void) -> some View](./view/onassigneddocumentdidwithdraw%28_%29.md)
  Adds an action to perform after an assigned document submission has been withdrawn.
- [func onAssignedDocumentWillSubmit((URL) async -> Bool) -> some View](./view/onassigneddocumentwillsubmit%28_%29.md)
  Adds an action to perform before submitting an assigned document.
- [func onAssignedDocumentWillWithdraw((URL) async -> Bool) -> some View](./view/onassigneddocumentwillwithdraw%28_%29.md)
  Adds an action to perform before withdrawing an assigned document submission.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](./view/onsubmit%28of,_%29.md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](./view/submitscope%28_%29.md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func submitLabel(SubmitLabel) -> some View](./view/submitlabel%28_%29.md)
  Sets the submit label for this view.
### Movement
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](./view/onmovecommand%28perform%29.md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func moveDisabled(Bool) -> some View](./view/movedisabled%28_%29.md)
  Adds a condition for whether the view’s view hierarchy is movable.
### Deletion
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](./view/ondeletecommand%28perform%29.md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func deleteDisabled(Bool) -> some View](./view/deletedisabled%28_%29.md)
  Adds a condition for whether the view’s view hierarchy is deletable.
### Commands
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](./view/pagecommand%28value,in,step%29.md)
  Steps a value through a range in response to page up or page down commands.
- [func onExitCommand(perform: (() -> Void)?) -> some View](./view/onexitcommand%28perform%29.md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](./view/onplaypausecommand%28perform%29.md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](./view/oncommand%28_,perform%29.md)
  Adds an action to perform in response to the given selector.
### Hinge
- [func onHingeChange(isEnabled: Bool, (DeviceHingeContext, DeviceHingeContext) -> Void) -> some View](./view/onhingechange%28isenabled,_%29.md)
  Adds an action to perform when the hinge context of the view hierarchy changes.
### Digital Crown
- [func digitalCrownAccessory(Visibility) -> some View](./view/digitalcrownaccessory%28_%29.md)
  Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](./view/digitalcrownaccessory%28content%29.md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./view/digitalcrownrotation%28_,from,through,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./view/digitalcrownrotation%28_,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](./view/digitalcrownrotation%28detent,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>) -> some View](./view/digitalcrownrotation%28_%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](./view/digitalcrownrotation%28_,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
### Game controller
- [func handlesGameControllerEvents(matching: GCUIEventTypes) -> some View](./view/handlesgamecontrollerevents%28matching%29.md)
  Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.
- [func handlesGameControllerEvents(matching: GCUIEventTypes, withOptions: GameControllerEventHandlingOptions?) -> some View](./view/handlesgamecontrollerevents%28matching,withoptions%29.md)
  Specifies the game controllers events which should be delivered through the GameController framework when the view or one of its descendants has focus.
### Immersive spaces
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](./view/onimmersionchange%28initial,_%29.md)
  Performs an action when the immersion state of your app changes.
- [func onWorldRecenter(action:)](./view/onworldrecenter%28action%29.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](./view/immersiveenvironmentpicker%28content%29.md)
  Add menu items to open immersive spaces from a media player’s environment picker.
### Volumes
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](./view/onvolumeviewpointchange%28updatestrategy,initial,_%29.md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](./view/supportedvolumeviewpoints%28_%29.md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
### User activities
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](./view/useractivity%28_,element,_%29.md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](./view/useractivity%28_,isactive,_%29.md)
  Advertises a user activity type.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](./view/oncontinueuseractivity%28_,perform%29.md)
  Registers a handler to invoke in response to a user activity that your app receives.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](./view/handlesexternalevents%28preferring,allowing%29.md)
  Specifies the external events that the view’s scene handles if the scene is already open.
### View life cycle
- [func onAppear(perform: (() -> Void)?) -> some View](./view/onappear%28perform%29.md)
  Adds an action to perform before this view appears.
- [func onDisappear(perform: (() -> Void)?) -> some View](./view/ondisappear%28perform%29.md)
  Adds an action to perform after this view disappears.
- [func onChange(of:initial:_:)](./view/onchange%28of,initial,_%29.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func task<T>(id: T, name: String?, executorPreference: any TaskExecutor, priority: TaskPriority, file: String, line: Int, sending () async -> Void) -> some View](./view/task%28id,name,executorpreference,priority,file,line,_%29.md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task<T>(id: T, name: String?, priority: TaskPriority, file: String, line: Int, sending () async -> Void) -> some View](./view/task%28id,name,priority,file,line,_%29.md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(name: String?, executorPreference: any TaskExecutor, priority: TaskPriority, file: String, line: Int, action: sending () async -> Void) -> some View](./view/task%28name,executorpreference,priority,file,line,action%29.md)
  Adds an asynchronous task to perform before this view appears.
- [func task(name: String?, priority: TaskPriority, file: String, line: Int, sending () async -> Void) -> some View](./view/task%28name,priority,file,line,_%29.md)
  Adds an asynchronous task to perform before this view appears.
### File renaming
- [func renameAction(_:)](./view/renameaction%28_%29.md)
  Sets a closure to run for the rename action.
### URLs
- [func onOpenURL(perform: (URL) -> ()) -> some View](./view/onopenurl%28perform%29.md)
  Registers a handler to invoke in response to a URL that your app receives.
- [func onOpenURL(prefersInApp: Bool) -> some View](./view/onopenurl%28prefersinapp%29.md)
  Sets an `OpenURLAction` that prefers opening URL with an in-app browser. The `handler` closure takes a URL as input, and returns a `OpenURLAction.Result` that indicates the outcome of the action.
- [func widgetURL(URL?) -> some View](./view/widgeturl%28_%29.md)
  Sets the URL to open in the containing app when the user clicks the widget.
### Asynchronous image loading
- [func asyncImageURLSession(URLSession) -> some View](./view/asyncimageurlsession%28_%29.md)
  A modifier that adds a URL session for asynchronous images contained in the view to use when fetching image data.
### Publisher events
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](./view/onreceive%28_,perform%29.md)
  Adds an action to perform when this view detects data emitted by the given publisher.
### Hit testing
- [func allowsHitTesting(Bool) -> some View](./view/allowshittesting%28_%29.md)
  Configures whether this view participates in hit test operations.
### Content shape
- [func contentShape<S>(S, eoFill: Bool) -> some View](./view/contentshape%28_,eofill%29.md)
  Defines the content shape for hit testing.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](./view/contentshape%28_,_,eofill%29.md)
  Sets the content shape for this view.
### Import and export
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some View](./view/exportsitemproviders%28_,onexport%29.md)
  Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit: ([NSItemProvider]) -> Bool) -> some View](./view/exportsitemproviders%28_,onexport,onedit%29.md)
  Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](./view/importsitemproviders%28_,onimport%29.md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](./view/exportabletoservices%28_%29.md)
  Exports items for consumption by shortcuts, quick actions, and services.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](./view/exportabletoservices%28_,onedit%29.md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.
- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](./view/importablefromservices%28for,action%29.md)
  Enables importing items from services, such as Continuity Camera on macOS.
### App intents
- [func appEntityIdentifier(EntityIdentifier?) -> some View](./view/appentityidentifier%28_%29.md)
  Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [func appEntityIdentifier<I>(forSelectionType: I.Type, identifier: (I) -> EntityIdentifier?) -> some View](./view/appentityidentifier%28forselectiontype,identifier%29.md)
  Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [func appEntityUIElements((AppEntityUIElementsContext) -> [AppEntityUIElement]) -> some View](./view/appentityuielements%28_%29.md)
  Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [func onAppIntentExecution<I>(I.Type, perform: (I) -> Void) -> some View](./view/onappintentexecution%28_,perform%29.md)
  Registers a handler to run when the app receives an app intent that targets the associated scene.
- [func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View](./view/shortcutslinkstyle%28_%29.md)
  Sets the given style for ShortcutsLinks within the view hierarchy
- [func siriTipViewStyle(SiriTipViewStyle) -> some View](./view/siritipviewstyle%28_%29.md)
  Sets the given style for SiriTipView within the view hierarchy
### Camera
- [func onCameraCaptureEvent(isEnabled: Bool, action: (AVCaptureEvent) -> Void) -> some View](./view/oncameracaptureevent%28isenabled,action%29.md)
  Used to register an action triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)](./view/oncameracaptureevent%28isenabled,defaultsounddisabled,action%29.md)
  Used to register an action triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)](./view/oncameracaptureevent%28isenabled,defaultsounddisabled,primaryaction,secondaryaction%29.md)
  Used to register actions triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled: Bool, primaryAction: (AVCaptureEvent) -> Void, secondaryAction: (AVCaptureEvent) -> Void) -> some View](./view/oncameracaptureevent%28isenabled,primaryaction,secondaryaction%29.md)
  Used to register actions triggered by system capture events.
- [func cameraAnchor(isActive: Bool) -> some View](./view/cameraanchor%28isactive%29.md)
  Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.

## See Also

### Providing interactivity
- [Search modifiers](./view-search.md)
  Enable people to search for content in your app.
- [Presentation modifiers](./view-presentation.md)
  Define additional views for the view to present under specified conditions.
- [State modifiers](./view-state.md)
  Access storage and provide child views with configuration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-input-and-events)*