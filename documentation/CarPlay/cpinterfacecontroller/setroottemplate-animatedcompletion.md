# setRootTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Sets the root template of the navigation hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool) async throws -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool) async throws -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If you set a root template when a navigation hierarchy already exists, CarPlay replaces the entire hierarchy.

CarPlay calls `completion` after it presents the template. The Boolean parameter is [`true`](https://developer.apple.com/documentation/swift/true) when the presentation succeeds; otherwise, it’s [`false`](https://developer.apple.com/documentation/swift/false) and CarPlay provides an error that describes the failure. CarPlay throws an exception if the presentation fails and you don’t provide a closure.

## Parameters

- `rootTemplate`: The template to use as the root of a new navigation hierarchy.
- `animated`: If  , CarPlay animates the presentation of the template. CarPlay ignores this flag when there isn’t an existing navigation hierarchy to replace.
- `completion`: The closure CarPlay calls after it presents the template.

## See Also

- [var delegate: (any CPInterfaceControllerDelegate)?](cpinterfacecontroller/delegate.md)
  An object that serves as the delegate to the interface controller.
- [protocol CPInterfaceControllerDelegate](cpinterfacecontrollerdelegate.md)
  The interface that an object implements to serve as a delegate to an interface controller.
- [var prefersDarkUserInterfaceStyle: Bool](cpinterfacecontroller/prefersdarkuserinterfacestyle.md)
  A Boolean value that determines whether the system draws the user interface in Dark Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/setroottemplate(_:animated:completion:))*