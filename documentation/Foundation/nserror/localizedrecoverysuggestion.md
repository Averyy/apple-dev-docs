# localizedRecoverySuggestion

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string containing the localized recovery suggestion for the error.

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
var localizedRecoverySuggestion: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * localizedRecoverySuggestion;
```

#### Discussion

The object in the user info dictionary for the key [`NSLocalizedRecoverySuggestionErrorKey`](../nslocalizedrecoverysuggestionerrorkey.md). If the user info dictionary doesn’t contain a value for [`NSLocalizedRecoverySuggestionErrorKey`](../nslocalizedrecoverysuggestionerrorkey.md), this property is `nil`.

The returned string is suitable for displaying as the secondary message in an alert panel.

## See Also

### Getting a Localized Error Description
- [var localizedDescription: String](./localizeddescription.md)
  A string containing the localized description of the error.
- [var localizedRecoveryOptions: [String]?](./localizedrecoveryoptions.md)
  An array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [var localizedFailureReason: String?](./localizedfailurereason.md)
  A string containing the localized explanation of the reason for the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/localizedrecoverysuggestion)*