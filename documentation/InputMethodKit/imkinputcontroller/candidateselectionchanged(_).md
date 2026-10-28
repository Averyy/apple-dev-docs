# candidateSelectionChanged(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Informs an input controller that the current candidate selection in the candidate window has changed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func candidateSelectionChanged(_ candidateString: NSAttributedString!)
```

```objc
- (void) candidateSelectionChanged:(NSAttributedString *) candidateString;
```

## Discussion

Note this method is called to indicate user activity in the candidate window. The candidate object might not be the user’s final selection.

## Parameters

- `candidateString`: The changed candidate string.

## See Also

### Tracking Selections
- [func annotationSelected(NSAttributedString!, forCandidate: NSAttributedString!)](./annotationselected%28_,forcandidate%29.md)
  Sends the selected candidate string and annotation string to the input controller.
- [func candidateSelected(NSAttributedString!)](./candidateselected%28_%29.md)
  Informs an input controller that a new candidate is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/candidateselectionchanged(_:))*