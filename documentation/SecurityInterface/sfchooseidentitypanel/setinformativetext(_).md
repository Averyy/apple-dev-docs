# setInformativeText(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the optional informative text displayed in the panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setInformativeText(_ informativeText: String!)
```

```objc
- (void) setInformativeText:(NSString *) informativeText;
```

## Parameters

- `informativeText`: A string containing a hostname, RFC 822 name (email address), URL, or similar identifier.

## See Also

### Customizing the Appearance of the Sheet or Panel
- [func setAlternateButtonTitle(String!)](./setalternatebuttontitle%28_%29.md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](./setdefaultbuttontitle%28_%29.md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](./policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
- [func informativeText() -> String!](./informativetext%28%29.md)
  Returns the informative text currently displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setinformativetext(_:))*