# setDefaultButtonTitle(_:)

**Framework**: Security Interface  
**Kind**: method

Customizes the title of the default button.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setDefaultButtonTitle(_ title: String!)
```

#### Discussion

The default button dismisses the sheet or panel and returns a value of [`NSOKButton`](https://developer.apple.com/documentation/AppKit/NSOKButton).

## Parameters

- `title`: The new title for the default button. The default title for this button is “OK”.

## See Also

- [func setAlternateButtonTitle(String!)](sfcertificatepanel/setalternatebuttontitle(_:).md)
  Customizes the title of the alternate button.
- [func setPolicies(Any!)](sfcertificatepanel/setpolicies(_:).md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](sfcertificatepanel/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/setdefaultbuttontitle(_:))*