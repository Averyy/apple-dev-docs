# update()

**Framework**: InputMethodKit  
**Kind**: method

Updates the candidates that are displayed in the candidates window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func update()
```

#### Discussion

When you call this method, the Input Method Kit  calls the candidates method of the [`IMKInputController`](imkinputcontroller.md) class. Note that the candidates list is updated, but the visible state of the window does not change. In other words, if the window is hidden, it remains hidden. If the window is visible, it remains visible.

## See Also

- [func show(IMKCandidatesLocationHint)](imkcandidates/show(_:).md)
  Shows the candidates window.
- [func hide()](imkcandidates/hide.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](imkcandidates/isvisible.md)
  Returns whether or not the candidates window is visible.
- [func setDismissesAutomatically(Bool)](imkcandidates/setdismissesautomatically(_:).md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func dismissesAutomatically() -> Bool](imkcandidates/dismissesautomatically.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/update())*