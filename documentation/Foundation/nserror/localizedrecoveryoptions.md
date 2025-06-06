# localizedRecoveryOptions

**Framework**: Foundation  
**Kind**: property

An array containing the localized titles of buttons appropriate for displaying in an alert panel.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var localizedRecoveryOptions: [String]? { get }
```

#### Discussion

The object in the user info dictionary for the key [`NSLocalizedRecoveryOptionsErrorKey`](nslocalizedrecoveryoptionserrorkey.md). If the user info dictionary doesn’t contain a value for [`NSLocalizedRecoveryOptionsErrorKey`](nslocalizedrecoveryoptionserrorkey.md), this property is `nil`.

The first string is the title of the right-most and default button, the second the one to the left of that, and so on. The recovery options should be appropriate for the  [`localizedRecoverySuggestion`](nserror/localizedrecoverysuggestion.md) property. If the user info dictionary doesn’t contain a value for [`NSLocalizedRecoveryOptionsErrorKey`](nslocalizedrecoveryoptionserrorkey.md), only an OK button is displayed.

## See Also

- [var localizedDescription: String](nserror/localizeddescription.md)
  A string containing the localized description of the error.
- [var localizedRecoverySuggestion: String?](nserror/localizedrecoverysuggestion.md)
  A string containing the localized recovery suggestion for the error.
- [var localizedFailureReason: String?](nserror/localizedfailurereason.md)
  A string containing the localized explanation of the reason for the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/localizedrecoveryoptions)*