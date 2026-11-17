# setRootTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Installs the root template of your app’s navigation hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool) async throws -> Bool
```

```objc
- (void) setRootTemplate:(CPTemplate *) rootTemplate animated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Mentions

- [Building your app’s initial CarPlay interface](../building-your-apps-initial-carplay-interface.md)

## Discussion

Call this method to install the root template of your app’s navigation interface. Typically, you call this method as part of the initial setup of your interface in the [`templateApplicationScene(_:didConnect:)`](../cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) or [`templateApplicationScene(_:didConnect:to:)`](../cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method of your scene delegate. If the interface controller already has a root template, this method removes the existing root template and all other pushed templates, and installs the new root template.

> **Note**: You can call this method from synchronous code using a completion handler, or you can call it as an asynchronous method without the completion handler. For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `rootTemplate`: The template to use as the root of your app’s navigation hierarchy. This template becomes the main interface for your app, so provide a template that people can use to navigate to the rest of your app’s content.
- `animated`: `true` if you want CarPlay to animate the presentation of the template. When you set the root template for the first time, CarPlay ignores this parameter. CarPlay uses this parameter only when you replace the root template.
- `completion`: The closure to run with the results of the operation. This closure receives a Boolean value and an optional error as parameters. The Boolean value is `true` if the installation of the new root template succeeded. If the value is `false`, CarPlay provides an error with information about what happened. If you don’t provide a closure, CarPlay throws an exception when an error occurs. CarPlay runs this closure on your app’s main thread.

## See Also

### Installing and removing templates
- [func pushTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pushtemplate%28_,animated,completion%29.md)
  Adds the specified template to the navigation hierarchy and displays it.
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptemplate%28animated,completion%29.md)
  Removes the top-most template from your app’s navigation hierarchy.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./poptoroottemplate%28animated,completion%29.md)
  Removes all of the templates from your app’s navigation hierarchy except the root template.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./pop%28to,animated,completion%29.md)
  Removes templates from your app’s navigation hierarchy until the specified template becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/setroottemplate(_:animated:completion:))*