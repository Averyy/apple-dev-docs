# presentTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Presents a template modally.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func presentTemplate(_ templateToPresent: CPTemplate, animated: Bool) async throws -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func presentTemplate(_ templateToPresent: CPTemplate, animated: Bool) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func presentTemplate(_ templateToPresent: CPTemplate, animated: Bool) async throws -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

CarPlay can only present one modal template at a time. `templateToPresent` must be one of [`CPActionSheetTemplate`](cpactionsheettemplate.md), [`CPAlertTemplate`](cpalerttemplate.md), or [`CPVoiceControlTemplate`](cpvoicecontroltemplate.md).

CarPlay calls `completion` after it presents the template. The Boolean parameter is [`true`](https://developer.apple.com/documentation/swift/true) when the presentation succeeds; otherwise, it’s [`false`](https://developer.apple.com/documentation/swift/false) and CarPlay provides an error that describes the failure. CarPlay throws an exception if the presentation fails and you don’t provide a closure.

## Parameters

- `templateToPresent`: The template to present modally.
- `animated`: If  , CarPlay animates the presentation of the template.
- `completion`: The closure CarPlay calls after it presents the template.

## See Also

- [func dismissTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/dismisstemplate(animated:completion:).md)
  Dismisses a modal template.
- [var presentedTemplate: CPTemplate?](cpinterfacecontroller/presentedtemplate.md)
  The interface controller’s current modal template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/presenttemplate(_:animated:completion:))*