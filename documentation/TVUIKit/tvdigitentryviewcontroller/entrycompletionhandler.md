# entryCompletionHandler

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

A completion handler that cues the app that the user has entered the required number of digits for the digit entry view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var entryCompletionHandler: (String) -> Void { get set }
```

```objc
@property (nonatomic, copy) void (^entryCompletionHandler)(NSString *entry);
```

## Discussion

Your app should respond with any required actions in response to the user’s entry.

## Parameters

- `entry`: The digits that the user entered into the digit entry view.

## See Also

### Entering Information
- [func clearEntry(animated: Bool)](./clearentry%28animated%29.md)
  Removes all digits from the digit entry view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller/entrycompletionhandler)*