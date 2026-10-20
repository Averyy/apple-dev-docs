# failureReason

**Framework**: ManagedAppDistribution  
**Kind**: property  
**Role**: Instance Property

A detailed description of the error.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
var failureReason: String? { get }
```

#### Discussion

This appears in the body of an alert.

## See Also

### Providing error information
- [var description: String](./description.md)
  A localized description of the error.
- [var errorDescription: String?](./errordescription.md)
  A brief description of the error.
- [var recoveryOptions: [String]](./recoveryoptions.md)
  A set of possible recovery options to present.
- [var recoverySuggestion: String?](./recoverysuggestion.md)
  A suggestion for recovering from the error.
- [var localizedStringResource: LocalizedStringResource](./localizedstringresource.md)
  A set of localized error strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappdistributionerror/failurereason)*