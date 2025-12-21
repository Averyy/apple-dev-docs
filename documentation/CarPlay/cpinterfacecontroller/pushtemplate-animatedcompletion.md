# pushTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Adds the specified template to the navigation hierarchy and displays it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
func pushTemplate(_ templateToPush: CPTemplate, animated: Bool) async throws -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func pushTemplate(_ templateToPush: CPTemplate, animated: Bool) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The template you add becomes the [`topTemplate`](cpinterfacecontroller/toptemplate.md) in the navigation hierarchy.

CarPlay calls `completion` after it adds the template to the navigation hierarchy. The Boolean parameter is [`true`](https://developer.apple.com/documentation/Swift/true) when CarPlay adds the template successfully; otherwise, it’s [`false`](https://developer.apple.com/documentation/Swift/false) and CarPlay provides an error that describes the failure.

CarPlay throws an exception if it can’t add the template and you don’t provide a closure.

## Parameters

- `templateToPush`: The template to add to the navigation hierarchy.
- `animated`: If  , CarPlay animates the transition between templates.
- `completion`: The closure CarPlay calls after it adds the template.

## See Also

- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/poptemplate(animated:completion:).md)
  Removes the top-most template from the navigation hierarchy.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/poptoroottemplate(animated:completion:).md)
  Removes all of the templates from the navigation hierarchy except the root template.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/pop(to:animated:completion:).md)
  Removes each template from the navigation hierarchy until the specified template becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/pushtemplate(_:animated:completion:))*