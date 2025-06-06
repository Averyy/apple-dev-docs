# State modifiers

**Framework**: SwiftUI

Access storage and provide child views with configuration data.

#### Overview

SwiftUI provides tools for managing data in your app. For example, you can store values and objects in an environment that’s shared among the views in a view hierarchy. Any view that shares the environment — typically all the descendant views of the view that stores the item — can then access the stored item.

For more information about the types that SwiftUI provides to help manage data in your app, see [`Model data`](model-data.md).

## Topics

### Identity
- [func tag<V>(V, includeOptional: Bool) -> some View](view/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func id<ID>(ID) -> some View](view/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func equatable() -> EquatableView<Self>](view/equatable.md)
  Prevents the view from updating its child view when its new value is the same as its old value.
### Environment values
- [func environment<T>(T?) -> some View](view/environment(_:).md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](view/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func environmentObject<T>(T) -> some View](view/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](view/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
### Preferences
- [func preference<K>(key: K.Type, value: K.Value) -> some View](view/preference(key:value:).md)
  Sets a value for the given preference.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](view/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](view/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](view/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](view/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](view/backgroundpreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](view/backgroundpreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](view/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](view/overlaypreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
### Default storage
- [func defaultAppStorage(UserDefaults) -> some View](view/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
### Configuring a model
- [func modelContext(ModelContext) -> some View](view/modelcontext(_:).md)
  Sets the model context in this view’s environment.
- [func modelContainer(ModelContainer) -> some View](view/modelcontainer(_:).md)
  Sets the model container and associated model context in this view’s environment.
- [func modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](view/modelcontainer(for:inmemory:isautosaveenabled:isundoenabled:onsetup:).md)
  Sets the model container in this view for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this view’s environment.

## See Also

- [Input and event modifiers](view-input-and-events.md)
  Supply actions for a view to perform in response to user input and system events.
- [Search modifiers](view-search.md)
  Enable people to search for content in your app.
- [Presentation modifiers](view-presentation.md)
  Define additional views for the view to present under specified conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-state)*