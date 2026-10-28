# setPoliciesDisclosed(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies whether the trust policy settings subview is disclosed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setPoliciesDisclosed(_ disclosed: Bool)
```

```objc
- (void) setPoliciesDisclosed:(BOOL) disclosed;
```

## Discussion

The trust policy settings can be shown or hidden depending on whether the user clicks the disclosure triangle. This method sets the state of that disclosure triangle and the visibility of the corresponding view.

## Parameters

- `disclosed`: Pass [`true`](../../Swift/true.md) to display the certificate details, or [`false`](../../Swift/false.md) to hide them.

## See Also

### Customizing the Appearance and Behavior of the View
- [func setDetailsDisclosed(Bool)](./setdetailsdisclosed%28_%29.md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](./setdisplaydetails%28_%29.md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](./setdisplaytrust%28_%29.md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](./seteditabletrust%28_%29.md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies the policies to use when evaluating this certificate’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setpoliciesdisclosed(_:))*