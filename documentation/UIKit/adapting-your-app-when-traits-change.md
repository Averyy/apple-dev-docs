# Adapting your app when traits change

**Framework**: UIKit

Find out when system changes happen that affect your app, then update your app efficiently.

#### Overview

When a person rotates their device, enables Dark Mode, or updates accessibility settings, the system updates the associated traits and propagates them through your app’s view hierarchy. You can monitor traits for changes, and then respond to those changes with code that adapts to the changed traits. For example, you might change what your view shows when either the [`horizontalSizeClass`](uitraitcollection/horizontalsizeclass.md) or [`verticalSizeClass`](uitraitcollection/verticalsizeclass.md) changes, or you might adjust what colors you use for light or dark appearance.

UIKit listens for trait changes automatically when you reference traits in specific methods, such as [`layoutSubviews()`](uiview/layoutsubviews().md).

Alternatively, when you want to listen for trait changes outside those methods, you can register to listen for specific traits using methods in the [`UITraitChangeObservable`](uitraitchangeobservable-67e94.md) protocol. Use this approach when your code that responds to a trait change isn’t appropriate for a method like [`layoutSubviews()`](uiview/layoutsubviews().md) that the system calls for each layout pass.

> 💡 **Tip**: If your app uses the deprecated [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) method to listen for trait changes, the system calls that method for every trait change, regardless of whether it needs to inform your code about the change. Migrate to either [`Automatic trait tracking`](automatic-trait-tracking.md) or [`UITraitChangeObservable`](uitraitchangeobservable-67e94.md) methods to avoid the extra calls and improve performance.

##### Track Trait Changes Automatically

To track a trait change automatically, add code that references a trait in one of the methods that UIKit supports for automatic trait tracking, such as [`horizontalSizeClass`](uitraitcollection/horizontalsizeclass.md) in [`layoutSubviews()`](uiview/layoutsubviews().md). In the following example, the implementation applies a layout appropriate for a smaller view when the size class is [`UIUserInterfaceSizeClass.compact`](uiuserinterfacesizeclass/compact.md), or a layout appropriate for a larger view when the size class is [`UIUserInterfaceSizeClass.regular`](uiuserinterfacesizeclass/regular.md):

```swift
class MyView: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()

        if traitCollection.horizontalSizeClass == .compact {
          // Apply compact layout.
        } else {
          // Apply regular layout.
        }
    }
}
```

When [`horizontalSizeClass`](uitraitcollection/horizontalsizeclass.md) changes, the system automatically invalidates the layout and calls [`layoutSubviews()`](uiview/layoutsubviews().md) in the next layout pass, so you can apply the correct layout for the size class.

For more information on the methods that UIKit supports for automatic trait tracking, see [`Automatic trait tracking`](automatic-trait-tracking.md).

##### Track Trait Changes with Registration

To track a specific trait or group of traits outside the automatic methods, use the registration methods in the [`UITraitChangeObservable`](uitraitchangeobservable-67e94.md) protocol. Select the trait or list of traits that you want to observe, and then specify a block of code or method to process each time those traits change. For example:

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    registerForTraitChanges([
        UITraitHorizontalSizeClass.self,
        UITraitVerticalSizeClass.self
    ]) { (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateLayout()
    }
}

func updateLayout() {
    let isCompact = traitCollection.horizontalSizeClass == .compact
    // Update your layout based on the size class.
}
```

Your handler executes whenever any of the registered traits change. If you need to determine which specific trait changed, compare the previous trait collection with the current one.

UIKit provides predefined trait sets that group related traits for common use cases, such as color change or image lookups. These semantic sets simplify your code when you need to respond to multiple related traits.

The following example uses [`systemTraitsAffectingColorAppearance`](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md) to register for all traits that affect color appearance, including user interface style, contrast level, and accessibility settings:

```swift
registerForTraitChanges(UITraitCollection.systemTraitsAffectingColorAppearance) {
    (self: Self, previousTraitCollection: UITraitCollection) in
    self.updateColors()
}
```

Other useful semantic trait sets include:

Trait registrations remain active for the lifetime of the object that created them. When the view or view controller deallocates, UIKit automatically removes all associated trait registrations, eliminating the need for manual cleanup in most cases.

If you need to unregister before deallocation, store the [`UITraitChangeRegistration`](uitraitchangeregistration.md) token the registration method returns and call the [`unregisterForTraitChanges(_:)`](uitraitchangeobservable-67e94/unregisterfortraitchanges(_:).md) method:

```swift
private var traitRegistration: UITraitChangeRegistration?

func startObservingTraits() {
    traitRegistration = registerForTraitChanges([UITraitHorizontalSizeClass.self]) {
        (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateLayout()
    }
}

func stopObservingTraits() {
    unregisterForTraitChanges(traitRegistration)
    traitRegistration = nil
}
```

##### Migrate From Deprecated Methods

If your code currently uses [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md), migrate to automatic trait tracking or trait registration for better performance and maintainability.

Remove implementations that check for trait changes in [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md), such as this example:

```swift
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)

    if traitCollection.horizontalSizeClass != previousTraitCollection?.horizontalSizeClass {
        updateLayout()
    }
}
```

Replace them with implementations in methods that support automatic trait tracking, such as this example:

```swift
override func layoutSubviews() {
    super.layoutSubviews()

    updateLayout(traitCollection.horizontalSizeClass)
}
```

Or, replace them with implementations that set up trait registrations in your setup code, as in the following example:

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    registerForTraitChanges([UITraitHorizontalSizeClass.self]) {
        (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateLayout()
    }
}
```

The automatic trait tracking and trait registration approaches are more efficient than using [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md), because your handler only executes when the traits you specify actually change, rather than on every trait change in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adapting-your-app-when-traits-change)*