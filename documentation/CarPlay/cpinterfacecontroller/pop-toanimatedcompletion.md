# pop(to:animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Removes each template from the navigation hierarchy until the specified template becomes visible.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func pop(to targetTemplate: CPTemplate, animated: Bool) async throws -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func pop(to targetTemplate: CPTemplate, animated: Bool) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func pop(to targetTemplate: CPTemplate, animated: Bool) async throws -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

`targetTemplate` must exist in the navigation hierarchy. You can use [`templates`](cpinterfacecontroller/templates.md) to access its contents.

CarPlay calls `completion` after it removes the required templates. The Boolean parameter is [`true`](https://developer.apple.com/documentation/swift/true) if the specified template exists in the navigation hierarchy and CarPlay removes the required templates successfully; otherwise, it’s [`false`](https://developer.apple.com/documentation/swift/false) and CarPlay provides an error that describes the failure.

CarPlay throws an exception if it can’t remove the required templates and you don’t provide a closure.

## Parameters

- `targetTemplate`: The template to make visible.
- `animated`: If  , CarPlay animates the transition between templates.
- `completion`: The closure CarPlay calls after it removes the required templates.

## See Also

- [func pushTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/pushtemplate(_:animated:completion:).md)
  Adds the specified template to the navigation hierarchy and displays it.
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/poptemplate(animated:completion:).md)
  Removes the top-most template from the navigation hierarchy.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/poptoroottemplate(animated:completion:).md)
  Removes all of the templates from the navigation hierarchy except the root template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/pop(to:animated:completion:))*