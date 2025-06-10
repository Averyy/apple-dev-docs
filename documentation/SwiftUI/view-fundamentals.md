# View fundamentals

**Framework**: SwiftUI

Define the visual elements of your app using a hierarchy of views.

#### Overview

Views are the building blocks that you use to declare your app’s user interface. Each view contains a description of what to display for a given state. Every bit of your app that’s visible to the user derives from the description in a view, and any type that conforms to the [`View`](view.md) protocol can act as a view in your app.

![None](https://docs-assets.developer.apple.com/published/61676615099d97b5303fa180a5e1b8d1/view-fundamentals-hero%402x.png)

Compose a custom view by combining built-in views that SwiftUI provides with other custom views that you create in your view’s [`body`](view/body-8kl5o.md) computed property. Configure views using the view modifiers that SwiftUI provides, or by defining your own view modifiers using the [`ViewModifier`](viewmodifier.md) protocol and the [`modifier(_:)`](view/modifier(_:).md) method.

## Topics

### Creating a view
- [Declaring a custom view](declaring-a-custom-view.md)
  Define views and assemble them into a view hierarchy.
- [protocol View](view.md)
  A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
- [struct ViewBuilder](viewbuilder.md)
  A custom parameter attribute that constructs views from closures.
### Modifying a view
- [Configuring views](configuring-views.md)
  Adjust the characteristics of a view by applying view modifiers.
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md)
  Bundle view modifiers that you regularly reuse into a custom view modifier.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](view/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [protocol ViewModifier](viewmodifier.md)
  A modifier that you apply to a view or another view modifier, producing a different version of the original value.
- [struct EmptyModifier](emptymodifier.md)
  An empty, or identity, modifier, used during development to switch modifiers at compile time.
- [struct ModifiedContent](modifiedcontent.md)
  A value with a modifier applied to it.
- [protocol EnvironmentalModifier](environmentalmodifier.md)
  A modifier that must resolve to a concrete modifier in an environment before use.
- [struct ManipulableModifier](manipulablemodifier.md)
- [struct ManipulableResponderModifier](manipulablerespondermodifier.md)
- [struct ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [struct ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [struct ManipulationGestureModifier](manipulationgesturemodifier.md)
- [struct ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [enum Manipulable](manipulable.md)
  A namespace for various manipulable related types.
### Responding to view life cycle updates
- [func onAppear(perform: (() -> Void)?) -> some View](view/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onDisappear(perform: (() -> Void)?) -> some View](view/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func task(priority: TaskPriority, () async -> Void) -> some View](view/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](view/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
### Managing the view hierarchy
- [func id<ID>(ID) -> some View](view/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func tag<V>(V, includeOptional: Bool) -> some View](view/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func equatable() -> EquatableView<Self>](view/equatable.md)
  Prevents the view from updating its child view when its new value is the same as its old value.
### Supporting view types
- [struct AnyView](anyview.md)
  A type-erased view.
- [struct EmptyView](emptyview.md)
  A view that doesn’t contain any content.
- [struct EquatableView](equatableview.md)
  A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [struct SubscriptionView](subscriptionview.md)
  A view that subscribes to a publisher with an action.
- [struct TupleView](tupleview.md)
  A View created from a swift tuple of View values.

## See Also

- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-fundamentals)*