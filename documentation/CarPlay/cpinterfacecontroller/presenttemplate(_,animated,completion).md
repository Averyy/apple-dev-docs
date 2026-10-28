# presentTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Presents a template modally.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func presentTemplate(_ templateToPresent: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func presentTemplate(_ templateToPresent: CPTemplate, animated: Bool) async throws -> Bool
```

```objc
- (void) presentTemplate:(CPTemplate *) templateToPresent animated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func presentTemplate(_ templateToPresent: CPTemplate, animated: Bool) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

CarPlay can only present one modal template at a time. `templateToPresent` must be one of [`CPActionSheetTemplate`](../cpactionsheettemplate.md), [`CPAlertTemplate`](../cpalerttemplate.md), or [`CPVoiceControlTemplate`](../cpvoicecontroltemplate.md).

CarPlay calls `completion` after it presents the template. The Boolean parameter is [`true`](../../Swift/true.md) when the presentation succeeds; otherwise, it’s [`false`](../../Swift/false.md) and CarPlay provides an error that describes the failure. CarPlay throws an exception if the presentation fails and you don’t provide a closure.

## Parameters

- `templateToPresent`: The template to present modally.
- `animated`: If [`true`](../../Swift/true.md), CarPlay animates the presentation of the template.
- `completion`: The closure CarPlay calls after it presents the template.

## See Also

### Displaying Templates Modally
- [func dismissTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./dismisstemplate%28animated,completion%29.md)
  Dismisses a modal template.
- [var presentedTemplate: CPTemplate?](./presentedtemplate.md)
  The interface controller’s current modal template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/presenttemplate(_:animated:completion:))*