# dismissTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Dismisses the template you previously presented modally.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func dismissTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func dismissTemplate(animated: Bool) async throws -> Bool
```

```objc
- (void) dismissTemplateAnimated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

Call this method to dismiss a template you presented using the [`presentTemplate(_:animated:completion:)`](./presenttemplate%28_,animated,completion%29.md) method.

> **Note**: You can call this method from synchronous code using a completion handler, or you can call it as an asynchronous method without the completion handler. For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `animated`: If `true`, CarPlay animates the dismissal of the modal presentation.
- `completion`: The closure to run with the results of the operation. This closure receives a Boolean value and an optional error as parameters. The Boolean value is `true` if CarPlay successfully dismissed the modal presentation. If the value is `false`, CarPlay provides an error with information about what happened. If you don’t provide a closure, CarPlay throws an exception when an error occurs. CarPlay runs this closure on your app’s main thread.

## See Also

### Presenting a template modally
- [func presentTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./presenttemplate%28_,animated,completion%29.md)
  Presents the template modally over your app’s navigation interface.
- [var presentedTemplate: CPTemplate?](./presentedtemplate.md)
  The current modally-presented template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/dismisstemplate(animated:completion:))*