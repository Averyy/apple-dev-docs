# NSLocalizedRecoverySuggestionErrorKey

**Framework**: Foundation  
**Kind**: var

The corresponding value is a string containing the localized recovery suggestion for the error.

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
let NSLocalizedRecoverySuggestionErrorKey: String
```

#### Discussion

This string is suitable for displaying as the secondary message in an alert panel.

## See Also

- [let NSURLErrorKey: String](nsurlerrorkey.md)
  The corresponding value is an `NSURL` object.
- [let NSFilePathErrorKey: String](nsfilepatherrorkey.md)
  Contains the file path of the error.
- [let NSHelpAnchorErrorKey: String](nshelpanchorerrorkey.md)
  The corresponding value is an `NSString` containing the localized help corresponding to the help button. See [`helpAnchor`](nserror/helpanchor.md) for more information.
- [let NSLocalizedDescriptionKey: String](nslocalizeddescriptionkey.md)
  The corresponding value is a localized string representation of the error that, if present, will be returned by [`localizedDescription`](nserror/localizeddescription.md).
- [let NSLocalizedFailureErrorKey: String](nslocalizedfailureerrorkey.md)
- [let NSLocalizedFailureReasonErrorKey: String](nslocalizedfailurereasonerrorkey.md)
  The corresponding value is a localized string representation containing the reason for the failure that, if present, will be returned by [`localizedFailureReason`](nserror/localizedfailurereason.md).
- [let NSLocalizedRecoveryOptionsErrorKey: String](nslocalizedrecoveryoptionserrorkey.md)
  The corresponding value is an array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [let NSRecoveryAttempterErrorKey: String](nsrecoveryattemptererrorkey.md)
  The corresponding value is an object that conforms to the NSErrorRecoveryAttempting informal protocol.
- [let NSStringEncodingErrorKey: String](nsstringencodingerrorkey.md)
  The corresponding value is an `NSNumber` object containing the `NSStringEncoding` value.
- [let NSUnderlyingErrorKey: String](nsunderlyingerrorkey.md)
  The corresponding value is an error that was encountered in an underlying implementation and caused the error that the receiver represents to occur.
- [let NSDebugDescriptionErrorKey: String](nsdebugdescriptionerrorkey.md)
- [let NSMultipleUnderlyingErrorsKey: String](nsmultipleunderlyingerrorskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocalizedrecoverysuggestionerrorkey)*