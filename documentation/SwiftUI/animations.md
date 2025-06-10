# Animations

**Framework**: SwiftUI

Create smooth visual updates in response to state changes.

#### Overview

You tell SwiftUI how to draw your app’s user interface for different states, and then rely on SwiftUI to make interface updates when the state changes.

![None](https://docs-assets.developer.apple.com/published/634da5b7eb74a20fee434a105cebd3c7/animations-hero%402x.png)

To avoid abrupt visual transitions when the state changes, add animation in one of the following ways:

- Animate all of the visual changes for a state change by changing the state inside a call to the [`withAnimation(_:_:)`](withanimation(_:_:).md) global function.
- Add animation to a particular view when a specific value changes by applying the [`animation(_:value:)`](view/animation(_:value:).md) view modifier to the view.
- Animate changes to a [`Binding`](binding.md) by using the binding’s [`animation(_:)`](binding/animation(_:).md) method.

SwiftUI animates the effects that many built-in view modifiers produce, like those that set a scale or opacity value. You can animate other values by making your custom views conform to the [`Animatable`](animatable.md) protocol, and telling SwiftUI about the value you want to animate.

When an animated state change results in adding or removing a view to or from the view hierarchy, you can tell SwiftUI how to transition the view into or out of place using built-in transitions that [`AnyTransition`](anytransition.md) defines, like [`slide`](anytransition/slide.md) or [`scale`](anytransition/scale.md). You can also create custom transitions.

For design guidance, see [`Motion`](https://developer.apple.com/design/Human-Interface-Guidelines/motion) in the Human Interface Guidelines.

## Topics

### Adding state-based animation to an action
- [func withAnimation<Result>(Animation?, () throws -> Result) rethrows -> Result](withanimation(_:_:).md)
  Returns the result of recomputing the view’s body with the provided animation.
- [func withAnimation<Result>(Animation?, completionCriteria: AnimationCompletionCriteria, () throws -> Result, completion: () -> Void) rethrows -> Result](withanimation(_:completioncriteria:_:completion:).md)
  Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [struct AnimationCompletionCriteria](animationcompletioncriteria.md)
  The criteria that determines when an animation is considered finished.
- [struct Animation](animation.md)
  The way a view changes over time to create a smooth visual transition from one state to another.
### Adding state-based animation to a view
- [func animation(_:)](view/animation(_:).md)
  Applies the given animation to this view when this view changes.
- [func animation<V>(Animation?, value: V) -> some View](view/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](view/animation(_:body:).md)
  Applies the given animation to all animatable values within the `body` closure.
### Creating phase-based animation
- [Controlling the timing and movements of your animations](controlling-the-timing-and-movements-of-your-animations.md)
  Build sophisticated animations that you control using phase and keyframe animators.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](view/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](view/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [struct PhaseAnimator](phaseanimator.md)
  A container that animates its content by automatically cycling through a collection of phases that you provide, each defining a discrete step within an animation.
### Creating keyframe-based animation
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [struct KeyframeAnimator](keyframeanimator.md)
  A container that animates its content with keyframes.
- [protocol Keyframes](keyframes.md)
  A type that defines changes to a value over time.
- [struct KeyframeTimeline](keyframetimeline.md)
  A description of how a value changes over time, modeled using keyframes.
- [struct KeyframeTrack](keyframetrack.md)
  A sequence of keyframes animating a single property of a root type.
- [struct KeyframeTrackContentBuilder](keyframetrackcontentbuilder.md)
  The builder that creates keyframe track content from the keyframes that you define within a closure.
- [struct KeyframesBuilder](keyframesbuilder.md)
  A builder that combines keyframe content values into a single value.
- [protocol KeyframeTrackContent](keyframetrackcontent.md)
  A group of keyframes that define an interpolation curve of an animatable value.
- [struct CubicKeyframe](cubickeyframe.md)
  A keyframe that uses a cubic curve to smoothly interpolate between values.
- [struct LinearKeyframe](linearkeyframe.md)
  A keyframe that uses simple linear interpolation.
- [struct MoveKeyframe](movekeyframe.md)
  A keyframe that immediately moves to the given value without interpolating.
- [struct SpringKeyframe](springkeyframe.md)
  A keyframe that uses a spring function to interpolate to the given value.
### Creating custom animations
- [protocol CustomAnimation](customanimation.md)
  A type that defines how an animatable value changes over time.
- [struct AnimationContext](animationcontext.md)
  Contextual values that a custom animation can use to manage state and access a view’s environment.
- [struct AnimationState](animationstate.md)
  A container that stores the state for a custom animation.
- [protocol AnimationStateKey](animationstatekey.md)
  A key for accessing animation state values.
- [struct UnitCurve](unitcurve.md)
  A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.
- [struct Spring](spring.md)
  A representation of a spring’s motion.
### Making data animatable
- [protocol Animatable](animatable.md)
  A type that describes how to animate a property of a view.
- [struct AnimatableValues](animatablevalues.md)
- [struct AnimatablePair](animatablepair.md)
  A pair of animatable values, which is itself animatable.
- [protocol VectorArithmetic](vectorarithmetic.md)
  A type that can serve as the animatable data of an animatable type.
- [struct EmptyAnimatableData](emptyanimatabledata.md)
  An empty type for animatable data.
### Updating a view on a schedule
- [Updating watchOS apps with timelines](../watchOS-Apps/updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [struct TimelineView](timelineview.md)
  A view that updates according to a schedule that you provide.
- [protocol TimelineSchedule](timelineschedule.md)
  A type that provides a sequence of dates for use as a schedule.
- [typealias TimelineViewDefaultContext](timelineviewdefaultcontext.md)
  Information passed to a timeline view’s content callback.
### Synchronizing geometries
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](view/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [struct MatchedGeometryProperties](matchedgeometryproperties.md)
  A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [protocol GeometryEffect](geometryeffect.md)
  An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [struct Namespace](namespace.md)
  A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [func geometryGroup() -> some View](view/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.
### Defining transitions
- [func transition(_:)](view/transition(_:).md)
  Associates a transition with the view.
- [protocol Transition](transition.md)
  A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [struct TransitionProperties](transitionproperties.md)
  The properties a `Transition` can have.
- [enum TransitionPhase](transitionphase.md)
  An indication of which the current stage of a transition.
- [struct AsymmetricTransition](asymmetrictransition.md)
  A composite `Transition` that uses a different transition for insertion versus removal.
- [struct AnyTransition](anytransition.md)
  A type-erased transition.
- [func contentTransition(ContentTransition) -> some View](view/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [var contentTransition: ContentTransition](environmentvalues/contenttransition.md)
  The current method of animating the contents of views.
- [var contentTransitionAddsDrawingGroup: Bool](environmentvalues/contenttransitionaddsdrawinggroup.md)
  A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [struct ContentTransition](contenttransition.md)
  A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [struct PlaceholderContentView](placeholdercontentview.md)
  A placeholder used to construct an inline modifier, transition, or other helper type.
- [func navigationTransition(some NavigationTransition) -> some View](view/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [protocol NavigationTransition](navigationtransition.md)
  A type that defines the transition to use when navigating to a view.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](view/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](view/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [protocol MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration.md)
  A configuration that defines the appearance of a matched transition source.
- [struct EmptyMatchedTransitionSourceConfiguration](emptymatchedtransitionsourceconfiguration.md)
  An unstyled matched transition source configuration.
### Moving an animation to another view
- [func withTransaction<Result>(Transaction, () throws -> Result) rethrows -> Result](withtransaction(_:_:).md)
  Executes a closure with the specified transaction and returns the result.
- [func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws -> R) rethrows -> R](withtransaction(_:_:_:).md)
  Executes a closure with the specified transaction key path and value and returns the result.
- [func transaction((inout Transaction) -> Void) -> some View](view/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](view/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](view/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [struct Transaction](transaction.md)
  The context of the current state-processing update.
- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.
- [protocol TransactionKey](transactionkey.md)
  A key for accessing values in a transaction.
### Deprecated types
- [protocol AnimatableModifier](animatablemodifier.md)
  A modifier that can create another modifier with animation.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animations)*