# Input events

**Framework**: SwiftUI  
**Role**: API Collection

Respond to input from a hardware device, like a keyboard or a Touch Bar.

## Overview

SwiftUI provides view modifiers that enable your app to listen for and react to various kinds of user input. For example, you can create keyboard shortcuts, respond to a form submission, or take input from the digital crown of an Apple Watch.

![](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/input-events-hero@2x.png)

For design guidance, see [Inputs](https://developer.apple.com/design/human-interface-guidelines/inputs) in the Human Interface Guidelines.

## Topics

### Responding to keyboard input
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
- [struct KeyPress](./keypress.md)
  A hardware keyboard event that a focused view receives.
### Creating keyboard shortcuts
- [func keyboardShortcut(_:)](./view/keyboardshortcut%28_%29.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](./view/keyboardshortcut%28_,modifiers%29.md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](./view/keyboardshortcut%28_,modifiers,localization%29.md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [var keyboardShortcut: KeyboardShortcut?](./environmentvalues/keyboardshortcut.md)
  The keyboard shortcut that buttons in this environment will be triggered with.
- [struct KeyboardShortcut](./keyboardshortcut.md)
  Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [struct KeyEquivalent](./keyequivalent.md)
  Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
- [struct EventModifiers](./eventmodifiers.md)
  A set of key modifiers that you can add to a gesture.
### Responding to modifier keys
- [func onModifierKeysChanged(mask: EventModifiers, initial: Bool, (EventModifiers, EventModifiers) -> Void) -> some View](./view/onmodifierkeyschanged%28mask,initial,_%29.md)
  Performs an action whenever the user presses or releases a hardware modifier key.
- [func modifierKeyAlternate<V>(EventModifiers, () -> V) -> some View](./view/modifierkeyalternate%28_,_%29.md)
  Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.
### Responding to hover events
- [func onHover(perform: (Bool) -> Void) -> some View](./view/onhover%28perform%29.md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func hoverEffect(_:isEnabled:)](./view/hovereffect%28_,isenabled%29.md)
  Applies a hover effect to this view.
- [func hoverEffectDisabled(Bool) -> some View](./view/hovereffectdisabled%28_%29.md)
  Adds a condition that controls whether this view can display hover effects.
- [func defaultHoverEffect(_:)](./view/defaulthovereffect%28_%29.md)
  Sets the default hover effect to use for views within this view.
- [var isHoverEffectEnabled: Bool](./environmentvalues/ishovereffectenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [enum HoverPhase](./hoverphase.md)
  The current hovering state and value of the pointer.
- [struct HoverEffectPhaseOverride](./hovereffectphaseoverride.md)
  Options for overriding a hover effect’s current phase.
- [struct OrnamentHoverContentEffect](./ornamenthovercontenteffect.md)
  Presents an ornament on hover using a custom effect.
- [struct OrnamentHoverEffect](./ornamenthovereffect.md)
  Presents an ornament on hover.
- [func onContinuousHover(coordinateSpace:perform:)](./view/oncontinuoushover%28coordinatespace,perform%29.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
### Modifying pointer appearance
- [func pointerStyle(PointerStyle?) -> some View](./view/pointerstyle%28_%29.md)
  Sets the pointer style to display when the pointer is over the view.
- [struct PointerStyle](./pointerstyle.md)
  A style describing the appearance of the pointer (also called a cursor) when it’s hovered over a view.
- [func pointerVisibility(Visibility) -> some View](./view/pointervisibility%28_%29.md)
  Sets the visibility of the pointer when it’s over the view.
### Changing view appearance for hover events
- [func hoverEffect(HoverEffect) -> some View](./view/hovereffect%28_%29.md)
  Applies a hover effect to this view.
- [struct HoverEffect](./hovereffect.md)
  An effect applied when the pointer hovers over a view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](./view/hovereffect%28_,in,isenabled%29.md)
  Applies a hover effect to this view, optionally adding it to a [`HoverEffectGroup`](./hovereffectgroup.md).
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](./view/hovereffect%28in,isenabled,body%29.md)
  Applies a hover effect to this view described by the given closure.
- [protocol CustomHoverEffect](./customhovereffect.md)
  A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [struct ContentHoverEffect](./contenthovereffect.md)
  A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [struct HoverEffectGroup](./hovereffectgroup.md)
  Describes a grouping of effects that activate together.
- [func hoverEffectGroup() -> some View](./view/hovereffectgroup%28%29.md)
  Adds an implicit [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](./view/hovereffectgroup%28_%29.md)
  Adds a [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](./view/hovereffectgroup%28id,in,behavior%29.md)
  Adds a [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [struct GroupHoverEffect](./grouphovereffect.md)
  A `CustomHoverEffect` that activates a named group of effects.
- [protocol HoverEffectContent](./hovereffectcontent.md)
  A type that describes the effects of a view for a particular hover effect phase.
- [struct EmptyHoverEffectContent](./emptyhovereffectcontent.md)
  An empty base effect that you use to build other effects.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](./view/handpointerbehavior%28_%29.md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [struct HandPointerBehavior](./handpointerbehavior.md)
  A behavior that can be applied to the hand pointer while the user is interacting with a view.
### Responding to submission events
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](./view/onsubmit%28of,_%29.md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](./view/submitscope%28_%29.md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [struct SubmitTriggers](./submittriggers.md)
  A type that defines various triggers that result in the firing of a submission action.
### Labeling a submission event
- [func submitLabel(SubmitLabel) -> some View](./view/submitlabel%28_%29.md)
  Sets the submit label for this view.
- [struct SubmitLabel](./submitlabel.md)
  A semantic label describing the label of submission within a view hierarchy.
### Responding to commands
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](./view/onmovecommand%28perform%29.md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](./view/ondeletecommand%28perform%29.md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](./view/pagecommand%28value,in,step%29.md)
  Steps a value through a range in response to page up or page down commands.
- [func onExitCommand(perform: (() -> Void)?) -> some View](./view/onexitcommand%28perform%29.md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](./view/onplaypausecommand%28perform%29.md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](./view/oncommand%28_,perform%29.md)
  Adds an action to perform in response to the given selector.
- [enum MoveCommandDirection](./movecommanddirection.md)
  Specifies the direction of an arrow key movement.
### Controlling hit testing
- [func allowsTightening(Bool) -> some View](./view/allowstightening%28_%29.md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func contentShape<S>(S, eoFill: Bool) -> some View](./view/contentshape%28_,eofill%29.md)
  Defines the content shape for hit testing.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](./view/contentshape%28_,_,eofill%29.md)
  Sets the content shape for this view.
- [struct ContentShapeKinds](./contentshapekinds.md)
  A kind for the content shape of a view.
### Responding to hinge angle changes
- [func onHingeChange(isEnabled: Bool, (DeviceHingeContext, DeviceHingeContext) -> Void) -> some View](./view/onhingechange%28isenabled,_%29.md)
  Adds an action to perform when the hinge context of the view hierarchy changes.
- [struct DeviceHingeContext](./devicehingecontext.md)
  A type describing the context of hinges on the device.
- [struct DeviceHinge](./devicehinge.md)
  A type encapsulating the state of a single hinge.
### Interacting with the Digital Crown
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
- [struct DigitalCrownEvent](./digitalcrownevent.md)
  An event emitted when the user rotates the Digital Crown.
- [enum DigitalCrownRotationalSensitivity](./digitalcrownrotationalsensitivity.md)
  The amount of Digital Crown rotation needed to move between two integer numbers.
### Managing Touch Bar input
- [func touchBar<Content>(content: () -> Content) -> some View](./view/touchbar%28content%29.md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](./view/touchbar%28_%29.md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarItemPrincipal(Bool) -> some View](./view/touchbaritemprincipal%28_%29.md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarCustomizationLabel(Text) -> some View](./view/touchbarcustomizationlabel%28_%29.md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](./view/touchbaritempresence%28_%29.md)
  Sets the behavior of the user-customized view.
- [struct TouchBar](./touchbar.md)
  A container for a view that you can show in the Touch Bar.
- [enum TouchBarItemPresence](./touchbaritempresence.md)
  Options that affect user customization of the Touch Bar.
### Responding to capture events
- [func onCameraCaptureEvent(isEnabled: Bool, action: (AVCaptureEvent) -> Void) -> some View](./view/oncameracaptureevent%28isenabled,action%29.md)
  Used to register an action triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled: Bool, primaryAction: (AVCaptureEvent) -> Void, secondaryAction: (AVCaptureEvent) -> Void) -> some View](./view/oncameracaptureevent%28isenabled,primaryaction,secondaryaction%29.md)
  Used to register actions triggered by system capture events.

## See Also

### Event handling
- [Gestures](./gestures.md)
  Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Clipboard](./clipboard.md)
  Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Drag and drop](./drag-and-drop.md)
  Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](./focus.md)
  Identify and control which visible object responds to user interaction.
- [System events](./system-events.md)
  React to system events, like opening a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/input-events)*