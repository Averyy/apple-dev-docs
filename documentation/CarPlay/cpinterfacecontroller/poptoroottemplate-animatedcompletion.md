# popToRootTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Removes all of the templates from the navigation hierarchy except the root template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
func popToRootTemplate(animated: Bool) async throws -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func popToRootTemplate(animated: Bool) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

CarPlay calls `completion` after it removes all of the required templates. The Boolean parameter is [`true`](https://developer.apple.com/documentation/Swift/true) if CarPlay removes all of the templates successfully; otherwise, it’s [`false`](https://developer.apple.com/documentation/Swift/false) and CarPlay provides an error that describes the failure.

CarPlay throws an exception if it can’t remove the templates and you don’t provide a closure.

## Parameters

- `animated`: If  , CarPlay animates the transition between templates.
- `completion`: The closure CarPlay calls after it removes the required templates.

## See Also

- [func pushTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/pushtemplate(_:animated:completion:).md)
  Adds the specified template to the navigation hierarchy and displays it.
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/poptemplate(animated:completion:).md)
  Removes the top-most template from the navigation hierarchy.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/pop(to:animated:completion:).md)
  Removes each template from the navigation hierarchy until the specified template becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/poptoroottemplate(animated:completion:))*