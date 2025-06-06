# showAnnotation(_:)

**Framework**: InputMethodKit  
**Kind**: method

Displays an annotation string in an annotation window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func showAnnotation(_ annotationString: NSAttributedString!)
```

#### Discussion

An annotation string explains or comments on the candidate string in the candidates window. An annotation window is a small, borderless window that is aligned with the current candidates window. An input method calls `showAnnotation:` when the `candidateSelectionChanged:` method of the [`IMKInputController`](imkinputcontroller.md) class is called, and the candidate string has annotations.

## Parameters

- `annotationString`: The string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/showannotation(_:))*