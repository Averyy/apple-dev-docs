# setAlternateButtonTitle(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Customizes the title of the alternate button.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setAlternateButtonTitle(_ title: String!)
```

```objc
- (void) setAlternateButtonTitle:(NSString *) title;
```

## Discussion

The alternate button is typically labelled “Cancel”. The alternate button dismisses the sheet or panel and returns a value of [`NSCancelButton`](../../AppKit/nscancelbutton.md).

## Parameters

- `title`: The new title for the alternate button. If this method is not called, or if `title` is set to `nil`, the button is not shown.

## See Also

### Related Documentation
- [func setDefaultButtonTitle(String!)](./setdefaultbuttontitle%28_%29.md)
  Customizes the title of the default button.
- [func runModal(for: SecTrust!, message: String!) -> Int](../sfcertificatetrustpanel/runmodal%28for,message%29.md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.
### Customizing the Appearance of the Sheet or Panel
- [func setDefaultButtonTitle(String!)](./setdefaultbuttontitle%28_%29.md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](./policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/setalternatebuttontitle(_:))*