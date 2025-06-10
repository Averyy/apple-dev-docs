# Informing ClassKit that a task is about to begin

**Framework**: ClassKit

Activate and deactivate contexts according to user interaction.

#### Overview

To provide hints to Schoolwork about which tasks are most recently and commonly used, activate the context that represents that task.

##### Activate Contexts When Users Begin Tasks

When a user navigates to a point in your app that corresponds to a particular context, you activate that context with a call to the [`becomeActive()`](clscontext/becomeactive().md) method.

In many cases, contexts correspond directly to views in your app. This lets you associate view appearance with context activation. For example, if your app presents one section of a chapter as a scroll view, and the corresponding view controller has a handle on the model instance representing that section, you can use the [`viewDidAppear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidAppear(_:)) method to activate the context:

```swift
override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)

    let path = section.identifierPath
    CLSDataStore.shared.mainAppContext.descendant(matchingIdentifierPath: path) { context, _ in
        context?.becomeActive()
    }
}
```

##### Deactivate Contexts When Users Finish

Similarly, you deactivate a context when the user leaves the corresponding area of your app using a call to the [`resignActive()`](clscontext/resignactive().md) method. In the case of the section view, you can add the call to the view controller’s [`viewWillDisappear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewWillDisappear(_:)) method:

```swift
override func viewWillDisappear(_ animated: Bool) {
    super.viewWillDisappear(animated)

    let path = section.identifierPath
    CLSDataStore.shared.mainAppContext.descendant(matchingIdentifierPath: path) { context, _ in
        context?.resignActive()
    }
}
```

Only one context can be active at a time. If you activate a new context when one is already active, the framework automatically causes the old one to resign.

> **Note**:  As demonstrated above, it’s always best to ask the framework for the context when you need it, rather than storing it in a class property. That’s because the underlying instance may change from time to time as a result of ongoing network synchronization. If you always ask for the context this way, you can be sure that you’re working with the right instance.

## See Also

- [func becomeActive()](clscontext/becomeactive.md)
  Tells a context to become the active context.
- [func resignActive()](clscontext/resignactive.md)
  Tells a context to stop being the active context.
- [var isActive: Bool](clscontext/isactive.md)
  A Boolean indicating whether the context is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/informing-classkit-that-a-task-is-about-to-begin)*