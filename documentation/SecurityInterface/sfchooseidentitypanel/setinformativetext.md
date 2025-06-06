# setInformativeText(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the optional informative text displayed in the panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setInformativeText(_ informativeText: String!)
```

## Parameters

- `informativeText`: A string containing a hostname, RFC 822 name (email address), URL, or similar identifier.

## See Also

- [func setAlternateButtonTitle(String!)](sfchooseidentitypanel/setalternatebuttontitle(_:).md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](sfchooseidentitypanel/setdefaultbuttontitle(_:).md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](sfchooseidentitypanel/setpolicies(_:).md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](sfchooseidentitypanel/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
- [func informativeText() -> String!](sfchooseidentitypanel/informativetext.md)
  Returns the informative text currently displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setinformativetext(_:))*