# setDismissesAutomatically(_:)

**Framework**: InputMethodKit  
**Kind**: method

Sets the state of the flag that determines whether the candidates window dismisses automatically.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setDismissesAutomatically(_ flag: Bool)
```

#### Discussion

By default, if the user presses the Return or Enter keys, the candidates are dismissed and a `candidateSelected:` message is sent to the input controller. You can call the `setDismissesAutomatically:` method, passing [`false`](https://developer.apple.com/documentation/Swift/false) as the `flag` parameter to change the default dismissal behavior. The input controller still receives a `candidatesSelected:` message.

When you set the flag to [`false`](https://developer.apple.com/documentation/Swift/false), an input method processes text input while dynamically updating the content of the candidates as the user inputs text. When a session deactivates, candidate window is hidden regardless of the state of the flag.

## Parameters

- `flag`:   to have the candidates window dismiss automatically; otherwise  .

## See Also

- [func show(IMKCandidatesLocationHint)](imkcandidates/show(_:).md)
  Shows the candidates window.
- [func hide()](imkcandidates/hide.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](imkcandidates/isvisible.md)
  Returns whether or not the candidates window is visible.
- [func dismissesAutomatically() -> Bool](imkcandidates/dismissesautomatically.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](imkcandidates/update.md)
  Updates the candidates that are displayed in the candidates window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/setdismissesautomatically(_:))*