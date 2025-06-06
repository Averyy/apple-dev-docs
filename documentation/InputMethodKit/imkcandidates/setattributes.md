# setAttributes(_:)

**Framework**: InputMethodKit  
**Kind**: method

Sets the style attributes for the candidates window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setAttributes(_ attributes: [AnyHashable : Any]!)
```

## Parameters

- `attributes`: A dictionary that contains keys and values for the styles to use. You can supply the keys and values listed in the following table:

## See Also

- [func panelType() -> IMKCandidatePanelType](imkcandidates/paneltype.md)
  Returns the style of the candidates window.
- [func setPanelType(IMKCandidatePanelType)](imkcandidates/setpaneltype(_:).md)
  Sets the style of the candidates window.
- [func attributes() -> [AnyHashable : Any]!](imkcandidates/attributes.md)
  Returns a dictionary of the style attributes used for the candidates window..


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/setattributes(_:))*