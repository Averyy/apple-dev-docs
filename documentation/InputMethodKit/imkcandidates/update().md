# update()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Updates the candidates that are displayed in the candidates window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func update()
```

```objc
- (void) updateCandidates;
```

#### Discussion

When you call this method, the Input Method Kit  calls the candidates method of the [`IMKInputController`](../imkinputcontroller.md) class. Note that the candidates list is updated, but the visible state of the window does not change. In other words, if the window is hidden, it remains hidden. If the window is visible, it remains visible.

## See Also

### Managing Window Visibility and Behavior
- [func show(IMKCandidatesLocationHint)](./show%28_%29.md)
  Shows the candidates window.
- [func hide()](./hide%28%29.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](./isvisible%28%29.md)
  Returns whether or not the candidates window is visible.
- [func setDismissesAutomatically(Bool)](./setdismissesautomatically%28_%29.md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func dismissesAutomatically() -> Bool](./dismissesautomatically%28%29.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/update())*