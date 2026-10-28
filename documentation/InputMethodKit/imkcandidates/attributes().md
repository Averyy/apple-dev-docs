# attributes()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary of the style attributes used for the candidates window..

**Availability**:
- macOS 10.5+

## Declaration

```swift
func attributes() -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) attributes;
```

## Return Value

The dictionary that contains the keys and values for the styles.

## See Also

### Managing Window Type and Text Attributes
- [func panelType() -> IMKCandidatePanelType](./paneltype%28%29.md)
  Returns the style of the candidates window.
- [func setPanelType(IMKCandidatePanelType)](./setpaneltype%28_%29.md)
  Sets the style of the candidates window.
- [func setAttributes([AnyHashable : Any]!)](./setattributes%28_%29.md)
  Sets the style attributes for the candidates window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/attributes())*