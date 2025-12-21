# dismissesAutomatically()

**Framework**: InputMethodKit  
**Kind**: method

Returns the state of the flag that determines whether the candidates window dismisses automatically.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func dismissesAutomatically() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the candidates window dismisses automatically; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func show(IMKCandidatesLocationHint)](imkcandidates/show(_:).md)
  Shows the candidates window.
- [func hide()](imkcandidates/hide.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](imkcandidates/isvisible.md)
  Returns whether or not the candidates window is visible.
- [func setDismissesAutomatically(Bool)](imkcandidates/setdismissesautomatically(_:).md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](imkcandidates/update.md)
  Updates the candidates that are displayed in the candidates window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/dismissesautomatically())*