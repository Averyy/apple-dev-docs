# setSelectedAttributes(_:isMultiple:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the Font panel that the specified font attributes changed for the selected text.

**Availability**:
- macOS

## Declaration

```swift
func setSelectedAttributes(_ attributes: [String : Any], isMultiple flag: Bool)
```

```objc
- (void) setSelectedAttributes:(NSDictionary<NSString *,id> *) attributes isMultiple:(BOOL) flag;
```

## Discussion

This method is used primarily by `NSTextView`.

## Parameters

- `attributes`: The new attributes.
- `flag`: If [`true`](../../Swift/true.md), informs the panel that multiple fonts or attributes are enclosed within the selection.

## See Also

### Setting Attributes
- [func convertAttributes([String : Any]) -> [String : Any]](./convertattributes%28_%29.md)
  Converts attributes in response to an object initiating an attribute change, typically the Font panel or Font menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setselectedattributes(_:ismultiple:))*