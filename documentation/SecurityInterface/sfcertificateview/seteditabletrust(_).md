# setEditableTrust(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies whether the user can edit the certificate’s trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setEditableTrust(_ editable: Bool)
```

```objc
- (void) setEditableTrust:(BOOL) editable;
```

## Discussion

For behavioral compatibility with macOS 10.3, this method causes the certificate trust settings to be displayed if they are not currently visible (that is, if [`setDisplayTrust(_:)`](./setdisplaytrust%28_%29.md) is set to [`false`](../../Swift/false.md)).

## Parameters

- `editable`: Pass [`true`](../../Swift/true.md) if the trust settings should be editable.

## See Also

### Related Documentation
- [func setDisplayTrust(Bool)](./setdisplaytrust%28_%29.md)
  Specifies whether the user can see the certificate’s trust settings.
### Customizing the Appearance and Behavior of the View
- [func setDetailsDisclosed(Bool)](./setdetailsdisclosed%28_%29.md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](./setdisplaydetails%28_%29.md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](./setdisplaytrust%28_%29.md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](./setpoliciesdisclosed%28_%29.md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/seteditabletrust(_:))*