# setSelectionKeysKeylayout(_:)

**Framework**: InputMethodKit  
**Kind**: method

Sets the key layout that is used to map virtual key codes to characters.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setSelectionKeysKeylayout(_ layout: TISInputSource!)
```

## Parameters

- `layout`: The key layout to use.

## See Also

- [func setSelectionKeys([Any]!)](imkcandidates/setselectionkeys(_:).md)
  Sets the selection keys for the candidates.
- [func selectionKeys() -> [Any]!](imkcandidates/selectionkeys.md)
  Returns an array of `NSNumber` objects where each `NSNumber` object represents a virtual key code.
- [func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!](imkcandidates/selectionkeyskeylayout.md)
  Returns the key layout that maps virtual key codes to selection keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/setselectionkeyskeylayout(_:))*