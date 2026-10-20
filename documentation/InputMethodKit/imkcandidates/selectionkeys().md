# selectionKeys()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of `NSNumber` objects where each `NSNumber` object represents a virtual key code.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func selectionKeys() -> [Any]!
```

```objc
- (NSArray *) selectionKeys;
```

#### Return Value

The array of `NSNumber` objects.

#### Discussion

Selection keys  are keys that can be used to select one of the candidates. They are displayed next to the candidate that will be selected when the user types that key.

## See Also

### Managing Selection Keys
- [func setSelectionKeys([Any]!)](./setselectionkeys%28_%29.md)
  Sets the selection keys for the candidates.
- [func setSelectionKeysKeylayout(TISInputSource!)](./setselectionkeyskeylayout%28_%29.md)
  Sets the key layout that is used to map virtual key codes to characters.
- [func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!](./selectionkeyskeylayout%28%29.md)
  Returns the key layout that maps virtual key codes to selection keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/selectionkeys())*