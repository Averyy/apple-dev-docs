# attachChild(_:toCandidate:type:)

**Framework**: InputMethodKit  
**Kind**: method

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func attachChild(_ child: IMKCandidates!, toCandidate candidateIdentifier: Int, type theType: IMKStyleType)
```

## See Also

- [func candidateFrame() -> NSRect](imkcandidates/candidateframe.md)
- [func candidateIdentifier(atLineNumber: Int) -> Int](imkcandidates/candidateidentifier(atlinenumber:).md)
- [func candidateStringIdentifier(Any!) -> Int](imkcandidates/candidatestringidentifier(_:).md)
- [func clearSelection()](imkcandidates/clearselection.md)
- [func detachChild(Int)](imkcandidates/detachchild(_:).md)
- [func hideChild()](imkcandidates/hidechild.md)
- [func lineNumberForCandidate(withIdentifier: Int) -> Int](imkcandidates/linenumberforcandidate(withidentifier:).md)
- [func selectCandidate(Int)](imkcandidates/selectcandidate(_:).md)
- [func selectCandidate(withIdentifier: Int) -> Bool](imkcandidates/selectcandidate(withidentifier:).md)
- [func selectedCandidate() -> Int](imkcandidates/selectedcandidate.md)
- [func selectedCandidateString() -> NSAttributedString!](imkcandidates/selectedcandidatestring.md)
- [func setCandidateData([Any]!)](imkcandidates/setcandidatedata(_:).md)
- [func setCandidateFrameTopLeft(NSPoint)](imkcandidates/setcandidateframetopleft(_:).md)
- [func show()](imkcandidates/show.md)
- [func showChild()](imkcandidates/showchild.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/attachchild(_:tocandidate:type:))*