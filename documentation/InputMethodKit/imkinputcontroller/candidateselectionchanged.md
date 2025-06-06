# candidateSelectionChanged(_:)

**Framework**: InputMethodKit  
**Kind**: method

Informs an input controller that the current candidate selection in the candidate window has changed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func candidateSelectionChanged(_ candidateString: NSAttributedString!)
```

#### Discussion

Note this method is called to indicate user activity in the candidate window. The candidate object might not be the user’s final selection.

## Parameters

- `candidateString`: The changed candidate string.

## See Also

- [func annotationSelected(NSAttributedString!, forCandidate: NSAttributedString!)](imkinputcontroller/annotationselected(_:forcandidate:).md)
  Sends the selected candidate string and annotation string to the input controller.
- [func candidateSelected(NSAttributedString!)](imkinputcontroller/candidateselected(_:).md)
  Informs an input controller that a new candidate is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/candidateselectionchanged(_:))*