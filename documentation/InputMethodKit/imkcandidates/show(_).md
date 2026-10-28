# show(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Shows the candidates window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func show(_ locationHint: IMKCandidatesLocationHint)
```

```objc
- (void) show:(IMKCandidatesLocationHint) locationHint;
```

## Discussion

Your input method  calls this method when it is appropriate during text conversion to display a list of candidates.

## Parameters

- `locationHint`: A [`IMKCandidatesLocationHint`](../imkcandidateslocationhint.md) constant that specifies the desired position of the candidates window. The Input Method Kit uses the hint to place the candidates window in a location that is in the vicinity of the hint location  and ensures that the candidates window is fully visible.

## See Also

### Managing Window Visibility and Behavior
- [func hide()](./hide%28%29.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](./isvisible%28%29.md)
  Returns whether or not the candidates window is visible.
- [func setDismissesAutomatically(Bool)](./setdismissesautomatically%28_%29.md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func dismissesAutomatically() -> Bool](./dismissesautomatically%28%29.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](./update%28%29.md)
  Updates the candidates that are displayed in the candidates window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/show(_:))*