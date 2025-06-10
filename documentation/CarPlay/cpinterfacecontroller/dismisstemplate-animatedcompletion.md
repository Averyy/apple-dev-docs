# dismissTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Dismisses a modal template.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
func dismissTemplate(animated: Bool) async throws -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func dismissTemplate(animated: Bool) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

CarPlay calls `completion` after it dismisses the template. The Boolean parameter is [`true`](https://developer.apple.com/documentation/swift/true) when the dismissal succeeds; otherwise, it’s [`false`](https://developer.apple.com/documentation/swift/false) and CarPlay provides an error that describes the failure. CarPlay throws an exception if the dismissal fails and you don’t provide a closure.

## Parameters

- `animated`: If  , CarPlay animates the dismissal of the template.
- `completion`: The closure CarPlay calls after it dismisses the template.

## See Also

- [func presentTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/presenttemplate(_:animated:completion:).md)
  Presents a template modally.
- [var presentedTemplate: CPTemplate?](cpinterfacecontroller/presentedtemplate.md)
  The interface controller’s current modal template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/dismisstemplate(animated:completion:))*