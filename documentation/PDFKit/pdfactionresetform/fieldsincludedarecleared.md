# fieldsIncludedAreCleared

**Framework**: PDFKit  
**Kind**: property

Sets whether the fields associated with the reset action are cleared when the action is performed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var fieldsIncludedAreCleared: Bool { get set }
```

## Parameters

- `include`: Pass   to clear the fields associated with the action when the reset action is performed. Pass   to exclude from the reset action only the fields associated with the action.

## See Also

- [class PDFActionResetForm](pdfactionresetform.md)
  `PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionresetform/fieldsincludedarecleared)*