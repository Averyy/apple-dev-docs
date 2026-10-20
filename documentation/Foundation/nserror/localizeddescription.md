# localizedDescription

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string containing the localized description of the error.

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
var localizedDescription: String { get }
```

```objc
@property (copy, readonly) NSString * localizedDescription;
```

#### Discussion

The object in the user info dictionary for the key [`NSLocalizedDescriptionKey`](../nslocalizeddescriptionkey.md). If the user info dictionary doesn’t contain a value for [`NSLocalizedDescriptionKey`](../nslocalizeddescriptionkey.md), a default string is constructed from the domain and code.

## See Also

### Related Documentation
- [var domain: String](./domain.md)
  A string containing the error domain.
- [var code: Int](./code.md)
  The error code.
- [var userInfo: [String : Any]](./userinfo.md)
  The user info dictionary.
### Getting a Localized Error Description
- [var localizedRecoveryOptions: [String]?](./localizedrecoveryoptions.md)
  An array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [var localizedRecoverySuggestion: String?](./localizedrecoverysuggestion.md)
  A string containing the localized recovery suggestion for the error.
- [var localizedFailureReason: String?](./localizedfailurereason.md)
  A string containing the localized explanation of the reason for the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/localizeddescription)*