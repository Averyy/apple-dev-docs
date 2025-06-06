# setSelectedAttributes(_:isMultiple:)

**Framework**: AppKit  
**Kind**: method

Informs the Font panel that the specified font attributes changed for the selected text.

**Availability**:
- macOS ?+

## Declaration

```swift
func setSelectedAttributes(_ attributes: [String : Any], isMultiple flag: Bool)
```

#### Discussion

This method is used primarily by `NSTextView`.

## Parameters

- `attributes`: The new attributes.
- `flag`: If  , informs the panel that multiple fonts or attributes are enclosed within the selection.

## See Also

- [func convertAttributes([String : Any]) -> [String : Any]](nsfontmanager/convertattributes(_:).md)
  Converts attributes in response to an object initiating an attribute change, typically the Font panel or Font menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setselectedattributes(_:ismultiple:))*