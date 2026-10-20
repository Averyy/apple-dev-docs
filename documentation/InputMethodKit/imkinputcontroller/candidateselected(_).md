# candidateSelected(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Informs an input controller that a new candidate is selected.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func candidateSelected(_ candidateString: NSAttributedString!)
```

```objc
- (void) candidateSelected:(NSAttributedString *) candidateString;
```

#### Discussion

The candidate object is the user’s final choice from the candidate window. The candidate window is closed before this method is called.

## Parameters

- `candidateString`: The changed candidate string.

## See Also

### Tracking Selections
- [func annotationSelected(NSAttributedString!, forCandidate: NSAttributedString!)](./annotationselected%28_,forcandidate%29.md)
  Sends the selected candidate string and annotation string to the input controller.
- [func candidateSelectionChanged(NSAttributedString!)](./candidateselectionchanged%28_%29.md)
  Informs an input controller that the current candidate selection in the candidate window has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/candidateselected(_:))*