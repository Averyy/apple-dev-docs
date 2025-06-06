# annotationSelected(_:forCandidate:)

**Framework**: InputMethodKit  
**Kind**: method

Sends the selected candidate string and annotation string to the input controller.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func annotationSelected(_ annotationString: NSAttributedString!, forCandidate candidateString: NSAttributedString!)
```

#### Discussion

This method is called when the user moves to a candidate.

## Parameters

- `annotationString`: The annotation string associated with the candidate.
- `candidateString`: The candidate string that the user moved to.

## See Also

- [func candidateSelectionChanged(NSAttributedString!)](imkinputcontroller/candidateselectionchanged(_:).md)
  Informs an input controller that the current candidate selection in the candidate window has changed.
- [func candidateSelected(NSAttributedString!)](imkinputcontroller/candidateselected(_:).md)
  Informs an input controller that a new candidate is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/annotationselected(_:forcandidate:))*