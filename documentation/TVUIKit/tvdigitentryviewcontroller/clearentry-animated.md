# clearEntry(animated:)

**Framework**: TVUIKit  
**Kind**: method

Removes all digits from the digit entry view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
func clearEntry(animated: Bool)
```

#### Discussion

The digit entry view animates the digit removal when the `animated` parameter is `YES`.

## Parameters

- `animated`: A Boolean value indicating whether the digit entry view animates when the digits are cleared.

## See Also

- [var entryCompletionHandler: (String) -> Void](tvdigitentryviewcontroller/entrycompletionhandler.md)
  A completion handler that cues the app that the user has entered the required number of digits for the digit entry view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller/clearentry(animated:))*