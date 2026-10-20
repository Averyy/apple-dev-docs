# setDisplayTrust(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies whether the user can see the certificate’s trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setDisplayTrust(_ display: Bool)
```

```objc
- (void) setDisplayTrust:(BOOL) display;
```

#### Discussion

Certificate trust settings are not displayed by default. To show the certificate’s trust settings, you must explicitly set the display value to [`true`](../../Swift/true.md). with either this method or the [`setEditableTrust(_:)`](./seteditabletrust%28_%29.md) method.

## Parameters

- `display`: Pass [`true`](../../Swift/true.md) to display the trust settings, or [`false`](../../Swift/false.md) to hide them.

## See Also

### Related Documentation
- [func isTrustDisplayed() -> Bool](./istrustdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s trust settings.
### Customizing the Appearance and Behavior of the View
- [func setDetailsDisclosed(Bool)](./setdetailsdisclosed%28_%29.md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](./setdisplaydetails%28_%29.md)
  Specifies whether the user can see the certificate details.
- [func setEditableTrust(Bool)](./seteditabletrust%28_%29.md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](./setpoliciesdisclosed%28_%29.md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setdisplaytrust(_:))*