# selectionKeysKeylayout()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Returns the key layout that maps virtual key codes to selection keys.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!
```

```objc
- (TISInputSourceRef) selectionKeysKeylayout;
```

## Return Value

The key layout in use. By default this is the key layout whose source id is `com.apple.keylayout.US`.

## See Also

### Managing Selection Keys
- [func setSelectionKeys([Any]!)](./setselectionkeys%28_%29.md)
  Sets the selection keys for the candidates.
- [func selectionKeys() -> [Any]!](./selectionkeys%28%29.md)
  Returns an array of `NSNumber` objects where each `NSNumber` object represents a virtual key code.
- [func setSelectionKeysKeylayout(TISInputSource!)](./setselectionkeyskeylayout%28_%29.md)
  Sets the key layout that is used to map virtual key codes to characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/selectionkeyskeylayout())*