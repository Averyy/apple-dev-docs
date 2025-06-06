# Using Key-Value Observing in Swift

**Framework**: Swift

Notify objects about changes to the properties of other objects.

#### Overview

Key-value observing is a Cocoa programming pattern you use to notify objects about changes to properties of other objects. It’s useful for communicating changes between logically separated parts of your app—such as between models and views. You can only use key-value observing with classes that inherit from [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class).

##### Annotate a Property for Key Value Observing

Mark properties that you want to observe through key-value observing with both the `@objc` attribute and the `dynamic` modifier. The example below defines the `MyObjectToObserve` class with a property—`myDate`—that can be observed:

```swift
class MyObjectToObserve: NSObject {
    @objc dynamic var myDate = NSDate(timeIntervalSince1970: 0) // 1970
    func updateDate() {
        myDate = myDate.addingTimeInterval(Double(2 << 30)) // Adds about 68 years.
    }
}
```

##### Define an Observer

An instance of an observer class manages information about changes made to one or more properties. When you create an observer, you start observation by calling the `observe(_:options:changeHandler:)` method with a key path that refers to the property you want to observe.

In the example below, the `\.objectToObserve.myDate` key path refers to the `myDate` property of `MyObjectToObserve`:

```swift
class MyObserver: NSObject {
    @objc var objectToObserve: MyObjectToObserve
    var observation: NSKeyValueObservation?

    init(object: MyObjectToObserve) {
        objectToObserve = object
        super.init()

        observation = observe(
            \.objectToObserve.myDate,
            options: [.old, .new]
        ) { object, change in
            print("myDate changed from: \(change.oldValue!), updated to: \(change.newValue!)")
        }
    }
}
```

You use the `oldValue` and `newValue` properties of the [`NSKeyValueObservedChange`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservedChange) instance to see what’s changed about the property you’re observing.

If you don’t need to know  a property has changed, omit the `options` parameter. Omitting the `options` parameter forgoes storing the new and old property values, which causes the `oldValue` and `newValue` properties to be `nil`.

##### Associate the Observer with the Property to Observe

You associate the property you want to observe with its observer by passing the object to the initializer of the observer:

```swift
let observed = MyObjectToObserve()
let observer = MyObserver(object: observed)
```

##### Respond to a Property Change

Objects that are set up to use key-value observing—such as `observed` above—notify their observers about property changes. The example below changes the `myDate` property by calling the `updateDate` method. That method call automatically triggers the observer’s change handler:

```swift
observed.updateDate() // Triggers the observer's change handler.
// Prints "myDate changed from: 1970-01-01 00:00:00 +0000, updated to: 2038-01-19 03:14:08 +0000"
```

The example above responds to the property change by printing both the new and old values of the date.

## See Also

- [Using Delegates to Customize Object Behavior](using-delegates-to-customize-object-behavior.md)
  Respond to events on behalf of a delegator.
- [Managing a Shared Resource Using a Singleton](managing-a-shared-resource-using-a-singleton.md)
  Provide access to a shared resource using a single, shared class instance.
- [About Imported Cocoa Error Parameters](about-imported-cocoa-error-parameters.md)
  Learn how Cocoa error parameters are converted to Swift throwing methods.
- [Handling Cocoa Errors in Swift](handling-cocoa-errors-in-swift.md)
  Throw and catch errors that use Cocoa’s error types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/using-key-value-observing-in-swift)*