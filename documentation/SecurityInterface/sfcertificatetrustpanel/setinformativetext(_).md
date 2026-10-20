# setInformativeText(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the (optional) informative text displayed in the panel.

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

- `informativeText`: By default, informative text describing the current certificate’s trust status is displayed. Call this method only if your application needs to customize the displayed informative text.

## See Also

### Controlling the Appearance of a Certificate Trust Panel
- [func informativeText() -> String!](./informativetext%28%29.md)
  Returns the (optional) informative text currently displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/setinformativetext(_:))*