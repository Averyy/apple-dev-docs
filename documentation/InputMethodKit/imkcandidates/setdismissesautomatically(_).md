# setDismissesAutomatically(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Sets the state of the flag that determines whether the candidates window dismisses automatically.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setDismissesAutomatically(_ flag: Bool)
```

```objc
- (void) setDismissesAutomatically:(BOOL) flag;
```

#### Discussion

By default, if the user presses the Return or Enter keys, the candidates are dismissed and a `candidateSelected:` message is sent to the input controller. You can call the `setDismissesAutomatically:` method, passing [`false`](../../Swift/false.md) as the `flag` parameter to change the default dismissal behavior. The input controller still receives a `candidatesSelected:` message.

When you set the flag to [`false`](../../Swift/false.md), an input method processes text input while dynamically updating the content of the candidates as the user inputs text. When a session deactivates, candidate window is hidden regardless of the state of the flag.

## Parameters

- `flag`: [`true`](../../Swift/true.md) to have the candidates window dismiss automatically; otherwise [`false`](../../Swift/false.md).

## See Also

### Managing Window Visibility and Behavior
- [func show(IMKCandidatesLocationHint)](./show%28_%29.md)
  Shows the candidates window.
- [func hide()](./hide%28%29.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](./isvisible%28%29.md)
  Returns whether or not the candidates window is visible.
- [func dismissesAutomatically() -> Bool](./dismissesautomatically%28%29.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](./update%28%29.md)
  Updates the candidates that are displayed in the candidates window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/setdismissesautomatically(_:))*