# pushTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Adds the specified template to the navigation hierarchy and displays it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func pushTemplate(_ templateToPush: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func pushTemplate(_ templateToPush: CPTemplate, animated: Bool) async throws -> Bool
```

```objc
- (void) pushTemplate:(CPTemplate *) templateToPush animated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func pushTemplate(_ templateToPush: CPTemplate, animated: Bool) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

The template you add becomes the [`topTemplate`](./toptemplate.md) in the navigation hierarchy.

CarPlay calls `completion` after it adds the template to the navigation hierarchy. The Boolean parameter is [`true`](../../Swift/true.md) when CarPlay adds the template successfully; otherwise, it’s [`false`](../../Swift/false.md) and CarPlay provides an error that describes the failure.

CarPlay throws an exception if it can’t add the template and you don’t provide a closure.

## Parameters

- `templateToPush`: The template to add to the navigation hierarchy.
- `animated`: If [`true`](../../Swift/true.md), CarPlay animates the transition between templates.
- `completion`: The closure CarPlay calls after it adds the template.

## See Also

### Adding and Removing Templates
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptemplate%28animated,completion%29.md)
  Removes the top-most template from the navigation hierarchy.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptoroottemplate%28animated,completion%29.md)
  Removes all of the templates from the navigation hierarchy except the root template.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pop%28to,animated,completion%29.md)
  Removes each template from the navigation hierarchy until the specified template becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/pushtemplate(_:animated:completion:))*