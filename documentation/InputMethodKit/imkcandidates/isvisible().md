# isVisible()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Returns whether or not the candidates window is visible.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func isVisible() -> Bool
```

```objc
- (BOOL) isVisible;
```

#### Return Value

[`true`](../../Swift/true.md) if the candidates window is visible; otherwise [`false`](../../Swift/false.md).

## See Also

### Managing Window Visibility and Behavior
- [func show(IMKCandidatesLocationHint)](./show%28_%29.md)
  Shows the candidates window.
- [func hide()](./hide%28%29.md)
  Hides a candidates window, if it is visible.
- [func setDismissesAutomatically(Bool)](./setdismissesautomatically%28_%29.md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func dismissesAutomatically() -> Bool](./dismissesautomatically%28%29.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](./update%28%29.md)
  Updates the candidates that are displayed in the candidates window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/isvisible())*