# entryCompletionHandler

**Framework**: TVUIKit  
**Kind**: property

A completion handler that cues the app that the user has entered the required number of digits for the digit entry view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var entryCompletionHandler: (String) -> Void { get set }
```

#### Discussion

Your app should respond with any required actions in response to the user’s entry.

## Parameters

- `entry`: The digits that the user entered into the digit entry view.

## See Also

- [func clearEntry(animated: Bool)](tvdigitentryviewcontroller/clearentry(animated:).md)
  Removes all digits from the digit entry view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller/entrycompletionhandler)*