# hideOverlayTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Dismisses the template previously displayed as an overlay.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func hideOverlayTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func hideOverlayTemplate(animated: Bool) async throws -> Bool
```

```objc
- (void) hideOverlayTemplateAnimated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

Call this method to dismiss a template you presented using the [`showOverlayTemplate(_:animated:completion:)`](./showoverlaytemplate%28_,animated,completion%29.md) method.

> **Note**: You can call this method from synchronous code using a completion handler, or you can call it as an asynchronous method without the completion handler. For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `animated`: If `true`, CarPlay animates the dismissal of the overlay.
- `completion`: The closure to run with the results of the operation. This closure receives a Boolean value and an optional error as parameters. The Boolean value is `true` if CarPlay successfully dismissed the overlay. If the value is `false`, CarPlay provides an error with information about what happened. If you don’t provide a closure, CarPlay throws an exception when an error occurs. CarPlay runs this closure on your app’s main thread.

## See Also

### Showing a template as an overlay
- [func showOverlayTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./showoverlaytemplate%28_,animated,completion%29.md)
  Displays a voice-control template as an overlay on top of your app’s current content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/hideoverlaytemplate(animated:completion:))*