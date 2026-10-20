# setPanelType(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Sets the style of the candidates window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setPanelType(_ panelType: IMKCandidatePanelType)
```

```objc
- (void) setPanelType:(IMKCandidatePanelType) panelType;
```

## Parameters

- `panelType`: A [`IMKCandidatePanelType`](../imkcandidatepaneltype.md) constant that represents the style of the candidates window.

## See Also

### Managing Window Type and Text Attributes
- [func panelType() -> IMKCandidatePanelType](./paneltype%28%29.md)
  Returns the style of the candidates window.
- [func setAttributes([AnyHashable : Any]!)](./setattributes%28_%29.md)
  Sets the style attributes for the candidates window.
- [func attributes() -> [AnyHashable : Any]!](./attributes%28%29.md)
  Returns a dictionary of the style attributes used for the candidates window..


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/setpaneltype(_:))*