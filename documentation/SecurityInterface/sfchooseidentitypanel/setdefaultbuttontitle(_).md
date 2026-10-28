# setDefaultButtonTitle(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Customizes the title of the default button.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setDefaultButtonTitle(_ title: String!)
```

```objc
- (void) setDefaultButtonTitle:(NSString *) title;
```

## Discussion

The default button dismisses the sheet or panel and returns a value of [`NSOKButton`](../../AppKit/nsokbutton.md).

## Parameters

- `title`: The new title for the default button. The default title for this button is “OK”.

## See Also

### Customizing the Appearance of the Sheet or Panel
- [func setAlternateButtonTitle(String!)](./setalternatebuttontitle%28_%29.md)
  Customizes the title of the alternate button.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](./policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
- [func informativeText() -> String!](./informativetext%28%29.md)
  Returns the informative text currently displayed in the panel.
- [func setInformativeText(String!)](./setinformativetext%28_%29.md)
  Sets the optional informative text displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setdefaultbuttontitle(_:))*