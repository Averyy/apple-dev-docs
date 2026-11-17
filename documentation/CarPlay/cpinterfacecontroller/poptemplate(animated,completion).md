# popTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Removes the top-most template from your app’s navigation hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func popTemplate(animated: Bool) async throws -> Bool
```

```objc
- (void) popTemplateAnimated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

Use this method to remove a template you previously added to the navigation stack with the [`pushTemplate(_:animated:completion:)`](./pushtemplate%28_,animated,completion%29.md) method. You can’t use this method to remove the root template, and this method reports an error if you try to do so. After the successful removal of the current top template, CarPlay displays the new top template on the navigation stack.

> **Note**: You can call this method from synchronous code using a completion handler, or you can call it as an asynchronous method without the completion handler. For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `animated`: If `true`, CarPlay animates the transition between templates.
- `completion`: The closure to run with the results of the operation. This closure receives a Boolean value and an optional error as parameters. The Boolean value is `true` if CarPlay successfully removes the top template. If the value is `false`, CarPlay provides an error with information about what happened. If you don’t provide a closure, CarPlay throws an exception when an error occurs. CarPlay runs this closure on your app’s main thread.

## See Also

### Installing and removing templates
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./setroottemplate%28_,animated,completion%29.md)
  Installs the root template of your app’s navigation hierarchy.
- [func pushTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pushtemplate%28_,animated,completion%29.md)
  Adds the specified template to the navigation hierarchy and displays it.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptoroottemplate%28animated,completion%29.md)
  Removes all of the templates from your app’s navigation hierarchy except the root template.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pop%28to,animated,completion%29.md)
  Removes templates from your app’s navigation hierarchy until the specified template becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/poptemplate(animated:completion:))*