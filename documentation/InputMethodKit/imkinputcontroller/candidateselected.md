# candidateSelected(_:)

**Framework**: InputMethodKit  
**Kind**: method

Informs an input controller that a new candidate is selected.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func candidateSelected(_ candidateString: NSAttributedString!)
```

#### Discussion

The candidate object is the user’s final choice from the candidate window. The candidate window is closed before this method is called.

## Parameters

- `candidateString`: The changed candidate string.

## See Also

- [func annotationSelected(NSAttributedString!, forCandidate: NSAttributedString!)](imkinputcontroller/annotationselected(_:forcandidate:).md)
  Sends the selected candidate string and annotation string to the input controller.
- [func candidateSelectionChanged(NSAttributedString!)](imkinputcontroller/candidateselectionchanged(_:).md)
  Informs an input controller that the current candidate selection in the candidate window has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/candidateselected(_:))*