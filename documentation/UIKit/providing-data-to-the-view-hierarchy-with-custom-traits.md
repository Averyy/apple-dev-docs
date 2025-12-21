# Providing data to the view hierarchy with custom traits

**Framework**: UIKit

Share data that needs to flow hierarchically across multiple levels of your view hierarchy.

#### Overview

A custom trait is a type that conforms to [`UITraitDefinition`](uitraitdefinition-3572h.md). Use a custom trait to pass application data, such as a color theme that a person selects in your app, through the objects in your view hierarchy that adopt [`UITraitEnvironment`](uitraitenvironment.md). Represent data with a custom trait when you want to:

- Propagate data to many children, such as contained view controllers or subviews.
- Pass data to distant components; for example, from a [`UIWindowScene`](uiwindowscene.md) subclass to a view inside a stack of view controllers.
- Provide context about the environment, such as information about a containing view controller from the current view controller, without a dependency on the containing view controller.

Avoid using custom traits for data that you can pass directly between view controllers and views.

##### Create Set and Access a Custom Trait

To create a custom trait, define a type that conforms to [`UITraitDefinition`](uitraitdefinition-3572h.md):

```swift
struct ContainedInSettingsTrait: UITraitDefinition {
    static let defaultValue = false
}
```

[`defaultValue`](uitraitdefinition-64c15/defaultvalue.md) is the only required static property. The system infers the type for your custom trait from the type of the value you set for `defaultValue`. After you define your custom trait, set its value using your trait as the key in the `traitOverrides` property of an object in your view hierarchy:

```swift
self.traitOverrides[ContainedInSettingsTrait.self] = true
```

Then, the system propagates the trait and value to that object’s descendants in the view hierarchy. For example, if the object is a view controller, the system propagates the view controller’s trait collection with the override to the view controller’s view and subviews, and to any child view controllers.

Access the value of your trait using your trait as the key in a trait collection:

```swift
let value = traitCollection[ContainedInSettingsTrait.self]
```

##### Simplify Custom Trait Access with Extensions

Add convenience properties to [`UITraitCollection`](uitraitcollection.md) and [`UIMutableTraits`](uimutabletraits-8l00o.md) to make your custom trait easier to access. First, extend [`UITraitCollection`](uitraitcollection.md) with a property to get the value of your custom trait from a trait collection:

```swift
extension UITraitCollection {
    var isContainedInSettings: Bool { self[ContainedInSettingsTrait.self] }
}
```

Next, extend [`UIMutableTraits`](uimutabletraits-8l00o.md) to get and set the value of your custom trait:

```swift
extension UIMutableTraits {
    var isContainedInSettings: Bool {
        get { self[ContainedInSettingsTrait.self] }
        set { self[ContainedInSettingsTrait.self] = newValue }
    }
}
```

Then, use standard property syntax to access and update your custom trait:

```swift
let traitCollection = UITraitCollection { mutableTraits in
    mutableTraits.isContainedInSettings = true
}

let value = traitCollection.isContainedInSettings
```

##### Enhance Custom Trait Interactions

Set optional properties of [`UITraitDefinition`](uitraitdefinition-3572h.md) to give your trait additional system capabilities and improve debugging:

The following example demonstrates setting these optional properties:

```swift
enum MyAppTheme: Int {
    case standard, pastel, bold, monochrome
}

struct MyAppThemeTrait: UITraitDefinition {
    static let defaultValue = MyAppTheme.standard
    static let affectsColorAppearance = true
    static let name = "Theme"
    static let identifier = "com.myapp.theme"
}
```

## See Also

- [protocol UIMutableTraits](uimutabletraits-13ja5.md)
  A mutable container of traits.
- [typealias UITrait](uitrait-9423.md)
  A type representing a trait in a trait collection.
- [protocol UITraitDefinition](uitraitdefinition-64c15.md)
  A type representing a trait in a trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/providing-data-to-the-view-hierarchy-with-custom-traits)*