# setAlternateButtonTitle(_:)

**Framework**: Security Interface  
**Kind**: method

Customizes the title of the alternate button.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setAlternateButtonTitle(_ title: String!)
```

#### Discussion

The alternate button is typically labelled “Cancel”. The alternate button dismisses the sheet or panel and returns a value of [`NSCancelButton`](https://developer.apple.com/documentation/AppKit/NSCancelButton).

## Parameters

- `title`: The new title for the alternate button. If this method is not called, or if   is set to  , the button is not shown.

## See Also

- [func setDefaultButtonTitle(String!)](sfcertificatepanel/setdefaultbuttontitle(_:).md)
  Customizes the title of the default button.
- [func runModal(for: SecTrust!, message: String!) -> Int](sfcertificatetrustpanel/runmodal(for:message:).md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.
- [func setDefaultButtonTitle(String!)](sfcertificatepanel/setdefaultbuttontitle(_:).md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](sfcertificatepanel/setpolicies(_:).md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](sfcertificatepanel/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/setalternatebuttontitle(_:))*