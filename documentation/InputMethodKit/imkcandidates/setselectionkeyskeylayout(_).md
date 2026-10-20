# setSelectionKeysKeylayout(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Sets the key layout that is used to map virtual key codes to characters.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setSelectionKeysKeylayout(_ layout: TISInputSource!)
```

```objc
- (void) setSelectionKeysKeylayout:(TISInputSourceRef) layout;
```

## Parameters

- `layout`: The key layout to use.

## See Also

### Managing Selection Keys
- [func setSelectionKeys([Any]!)](./setselectionkeys%28_%29.md)
  Sets the selection keys for the candidates.
- [func selectionKeys() -> [Any]!](./selectionkeys%28%29.md)
  Returns an array of `NSNumber` objects where each `NSNumber` object represents a virtual key code.
- [func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!](./selectionkeyskeylayout%28%29.md)
  Returns the key layout that maps virtual key codes to selection keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/setselectionkeyskeylayout(_:))*