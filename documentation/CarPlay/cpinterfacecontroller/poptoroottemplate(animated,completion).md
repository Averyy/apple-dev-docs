# popToRootTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Removes all of the templates from the navigation hierarchy except the root template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func popToRootTemplate(animated: Bool) async throws -> Bool
```

```objc
- (void) popToRootTemplateAnimated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func popToRootTemplate(animated: Bool) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

CarPlay calls `completion` after it removes all of the required templates. The Boolean parameter is [`true`](../../Swift/true.md) if CarPlay removes all of the templates successfully; otherwise, it’s [`false`](../../Swift/false.md) and CarPlay provides an error that describes the failure.

CarPlay throws an exception if it can’t remove the templates and you don’t provide a closure.

## Parameters

- `animated`: If [`true`](../../Swift/true.md), CarPlay animates the transition between templates.
- `completion`: The closure CarPlay calls after it removes the required templates.

## See Also

### Adding and Removing Templates
- [func pushTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pushtemplate%28_,animated,completion%29.md)
  Adds the specified template to the navigation hierarchy and displays it.
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptemplate%28animated,completion%29.md)
  Removes the top-most template from the navigation hierarchy.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pop%28to,animated,completion%29.md)
  Removes each template from the navigation hierarchy until the specified template becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/poptoroottemplate(animated:completion:))*