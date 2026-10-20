# setDisplayDetails(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies whether the user can see the certificate details.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setDisplayDetails(_ display: Bool)
```

```objc
- (void) setDisplayDetails:(BOOL) display;
```

#### Discussion

For behavioral compatibility with macOS 10.3, certificate details are displayed by default. To hide the details of a certificate, you must explicitly set the display value to [`false`](../../Swift/false.md).

## Parameters

- `display`: Pass [`true`](../../Swift/true.md) to display the certificate details, or [`false`](../../Swift/false.md) to hide them.

## See Also

### Related Documentation
- [func detailsDisplayed() -> Bool](./detailsdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s details.
### Customizing the Appearance and Behavior of the View
- [func setDetailsDisclosed(Bool)](./setdetailsdisclosed%28_%29.md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayTrust(Bool)](./setdisplaytrust%28_%29.md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](./seteditabletrust%28_%29.md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](./setpoliciesdisclosed%28_%29.md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setdisplaydetails(_:))*