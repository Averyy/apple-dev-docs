# setInformativeText(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the (optional) informative text displayed in the panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setInformativeText(_ informativeText: String!)
```

## Parameters

- `informativeText`: By default, informative text describing the current certificate’s trust status is displayed. Call this method only if your application needs to customize the displayed informative text.

## See Also

- [func informativeText() -> String!](sfcertificatetrustpanel/informativetext.md)
  Returns the (optional) informative text currently displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/setinformativetext(_:))*