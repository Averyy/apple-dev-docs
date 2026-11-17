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

Call this method to update your navigation interface and display different content. Typically, you use this method to navigate deeper into your app’s content. For example, when someone selects a playlist in a music app, the app pushes a list template with the songs in the playlist. This method requires an already installed root template, which you install using the [`setRootTemplate(_:animated:completion:)`](./setroottemplate%28_,animated,completion%29.md) method. If no root template exists, the method reports an error.

The type of app you create determines the maximum number of templates you can push onto your app’s navigation stack. The following table lists the total number of templates each app type supports; the root template counts as the first template in the total. For example, an audio app can push four additional templates after installing the root template.

| App type | Maximum stack depth |
| --- | --- |
| Audio | 5 templates |
| Communication | 5 templates |
| Driving task | 3 templates (2 templates in iOS 26.3 and earlier) |
| EV charging | 5 templates |
| Fueling | 3 templates |
| Navigation | 5 templates |
| Parking | 5 templates |
| Public safety | 5 templates |
| Quick food ordering | 3 templates (2 templates in iOS 26.3 and earlier) |
| Video | 5 templates |
| Voice-based conversation | 3 templates |

> **Note**: You can call this method from synchronous code using a completion handler, or you can call it as an asynchronous method without the completion handler. For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `templateToPush`: The template to add to the navigation hierarchy. After a successful push operation, this template becomes the top template in the navigation hierarchy, and you can access it from the [`topTemplate`](./toptemplate.md) property.
- `animated`: If `true`, CarPlay animates the transition between templates.
- `completion`: The closure to run with the results of the operation. This closure receives a Boolean value and an optional error as parameters. The Boolean value is `true` if CarPlay successfully pushed the new template. If the value is `false`, CarPlay provides an error with information about what happened. If you don’t provide a closure, CarPlay throws an exception when an error occurs. CarPlay runs this closure on your app’s main thread.

## See Also

### Installing and removing templates
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./setroottemplate%28_,animated,completion%29.md)
  Installs the root template of your app’s navigation hierarchy.
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptemplate%28animated,completion%29.md)
  Removes the top-most template from your app’s navigation hierarchy.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptoroottemplate%28animated,completion%29.md)
  Removes all of the templates from your app’s navigation hierarchy except the root template.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pop%28to,animated,completion%29.md)
  Removes templates from your app’s navigation hierarchy until the specified template becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/pushtemplate(_:animated:completion:))*