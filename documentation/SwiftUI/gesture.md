# Gesture

**Framework**: SwiftUI  
**Kind**: protocol

An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol Gesture<Value>
```

#### Overview

Create custom gestures by declaring types that conform to the `Gesture` protocol.

## Topics

### Implementing a custom gesture
- [var body: Self.Body](gesture/body-swift.property.md)
  The content and behavior of the gesture.
- [associatedtype Body : Gesture](gesture/body-swift.associatedtype.md)
  The type of gesture representing the body of `Self`.
### Performing the gesture
- [func updating<State>(GestureState<State>, body: (Self.Value, inout State, inout Transaction) -> Void) -> GestureStateGesture<Self, State>](gesture/updating(_:body:).md)
  Updates the provided gesture state property as the gesture’s value changes.
- [func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>](gesture/onchanged(_:).md)
  Adds an action to perform when the gesture’s value changes.
- [func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>](gesture/onended(_:).md)
  Adds an action to perform when the gesture ends.
- [associatedtype Value](gesture/value.md)
  The type representing the gesture’s value.
### Composing gestures
- [func simultaneously<Other>(with: Other) -> SimultaneousGesture<Self, Other>](gesture/simultaneously(with:).md)
  Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.
- [func sequenced<Other>(before: Other) -> SequenceGesture<Self, Other>](gesture/sequenced(before:).md)
  Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.
- [func exclusively<Other>(before: Other) -> ExclusiveGesture<Self, Other>](gesture/exclusively(before:).md)
  Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.
### Adding modifier keys to a gesture
- [func modifiers(EventModifiers) -> _ModifiersGesture<Self>](gesture/modifiers(_:).md)
  Combines a gesture with keyboard modifiers.
### Transforming a gesture
- [func map<T>((Self.Value) -> T) -> _MapGesture<Self, T>](gesture/map(_:).md)
  Returns a gesture that uses the given closure to map over this gesture’s value.
### Customizing gesture activation
- [func handActivationBehavior(HandActivationBehavior) -> some Gesture<Self.Value>
](gesture/handactivationbehavior(_:).md)
  Customizes the activation behavior for a gesture when driven by hand or hand-like input.
### Using a gesture with a RealityKit entity
- [func targetedToAnyEntity() -> some Gesture<EntityTargetValue<Self.Value>>
](gesture/targetedtoanyentity.md)
  Requires this gesture to target an entity.
- [func targetedToEntity(Entity) -> some Gesture<EntityTargetValue<Self.Value>>
](gesture/targetedtoentity(_:).md)
  Requires this gesture to target an entity or a descendant of entity.
- [func targetedToEntity(where: QueryPredicate<Entity>) -> some Gesture<EntityTargetValue<Self.Value>>
](gesture/targetedtoentity(where:).md)
  Requires this gesture to target an entity that can be found in the results of the query.

## Relationships

### Conforming Types
- [AnyGesture](anygesture.md)
- [DragGesture](draggesture.md)
- [ExclusiveGesture](exclusivegesture.md)
- [GestureStateGesture](gesturestategesture.md)
- [LongPressGesture](longpressgesture.md)
- [MagnificationGesture](magnificationgesture.md)
- [MagnifyGesture](magnifygesture.md)
- [RotateGesture](rotategesture.md)
- [RotateGesture3D](rotategesture3d.md)
- [RotationGesture](rotationgesture.md)
- [SequenceGesture](sequencegesture.md)
- [SimultaneousGesture](simultaneousgesture.md)
- [SpatialEventGesture](spatialeventgesture.md)
- [SpatialTapGesture](spatialtapgesture.md)
- [TapGesture](tapgesture.md)
- [WindowDragGesture](windowdraggesture.md)

## See Also

- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](view/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](view/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](view/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func defersSystemGestures(on: Edge.Set) -> some View](view/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [struct AnyGesture](anygesture.md)
  A type-erased gesture.
- [struct HandActivationBehavior](handactivationbehavior.md)
  An activation behavior specific to hand-driven input.
- [struct HandGestureShortcut](handgestureshortcut.md)
  Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture)*