# setAlternateButtonTitle(_:)

**Framework**: Security Interface  
**Kind**: method

Customizes the title of the alternate button.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setAlternateButtonTitle(_ title: String!)
```

#### Discussion

The alternate button is typically labelled “Cancel”. The alternate button dismisses the sheet or panel and returns a value of [`NSCancelButton`](https://developer.apple.com/documentation/AppKit/NSCancelButton).

## Parameters

- `title`: The new title for the alternate button. If this method is not called, or if   is set to  , the button is not shown.

## See Also

- [func setDefaultButtonTitle(String!)](sfchooseidentitypanel/setdefaultbuttontitle(_:).md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](sfchooseidentitypanel/setpolicies(_:).md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](sfchooseidentitypanel/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
- [func informativeText() -> String!](sfchooseidentitypanel/informativetext.md)
  Returns the informative text currently displayed in the panel.
- [func setInformativeText(String!)](sfchooseidentitypanel/setinformativetext(_:).md)
  Sets the optional informative text displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setalternatebuttontitle(_:))*