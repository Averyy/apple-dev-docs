# Environment values

**Framework**: SwiftUI

Share data throughout a view hierarchy using the environment.

#### Overview

Views in SwiftUI can react to configuration information that they read from the environment using an [`Environment`](environment.md) property wrapper.

![None](https://docs-assets.developer.apple.com/published/c55679ce6979b83be86939cf3c9b5b65/environment-values-hero%402x.png)

A view inherits its environment from its container view, subject to explicit changes from an [`environment(_:_:)`](view/environment(_:_:).md) view modifier, or by implicit changes from one of the many modifiers that operate on environment values. As a result, you can configure a entire hierarchy of views by modifying the environment of the group’s container.

You can find many built-in environment values in the [`EnvironmentValues`](environmentvalues.md) structure. You can also create a custom [`EnvironmentValues`](environmentvalues.md) property by defining a new property in an extension to the environment values structure and applying the [`Entry()`](entry().md) macro to the variable declaration.

## Topics

### Accessing environment values
- [struct Environment](environment.md)
  A property wrapper that reads a value from a view’s environment.
- [struct EnvironmentValues](environmentvalues.md)
  A collection of environment values propagated through a view hierarchy.
### Creating custom environment values
- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.
- [protocol EnvironmentKey](environmentkey.md)
  A key for accessing values in the environment.
### Modifying the environment of a view
- [func environment<T>(T?) -> some View](view/environment(_:).md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](view/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](view/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
### Modifying the environment of a scene
- [func environment<T>(T?) -> some Scene](scene/environment(_:).md)
  Places an observable object in the scene’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some Scene](scene/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some Scene](scene/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.

## See Also

- [Model data](model-data.md)
  Manage the data that your app uses to drive its interface.
- [Preferences](preferences.md)
  Indicate configuration preferences from views to their container views.
- [Persistent storage](persistent-storage.md)
  Store data for use across sessions of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environment-values)*