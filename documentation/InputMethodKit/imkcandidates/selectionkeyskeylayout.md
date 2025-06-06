# selectionKeysKeylayout()

**Framework**: InputMethodKit  
**Kind**: method

Returns the key layout that maps virtual key codes to selection keys.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!
```

#### Return Value

The key layout in use. By default this is the key layout whose source id is `com.apple.keylayout.US`.

## See Also

- [func setSelectionKeys([Any]!)](imkcandidates/setselectionkeys(_:).md)
  Sets the selection keys for the candidates.
- [func selectionKeys() -> [Any]!](imkcandidates/selectionkeys.md)
  Returns an array of `NSNumber` objects where each `NSNumber` object represents a virtual key code.
- [func setSelectionKeysKeylayout(TISInputSource!)](imkcandidates/setselectionkeyskeylayout(_:).md)
  Sets the key layout that is used to map virtual key codes to characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/selectionkeyskeylayout())*