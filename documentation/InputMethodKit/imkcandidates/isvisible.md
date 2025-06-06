# isVisible()

**Framework**: InputMethodKit  
**Kind**: method

Returns whether or not the candidates window is visible.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func isVisible() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the candidates window is visible; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func show(IMKCandidatesLocationHint)](imkcandidates/show(_:).md)
  Shows the candidates window.
- [func hide()](imkcandidates/hide.md)
  Hides a candidates window, if it is visible.
- [func setDismissesAutomatically(Bool)](imkcandidates/setdismissesautomatically(_:).md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func dismissesAutomatically() -> Bool](imkcandidates/dismissesautomatically.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](imkcandidates/update.md)
  Updates the candidates that are displayed in the candidates window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/isvisible())*