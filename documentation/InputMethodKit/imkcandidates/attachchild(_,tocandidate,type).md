# attachChild(_:toCandidate:type:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.7+

## Declaration

```swift
func attachChild(_ child: IMKCandidates!, toCandidate candidateIdentifier: Int, type theType: IMKStyleType)
```

```objc
- (void) attachChild:(IMKCandidates *) child toCandidate:(NSInteger) candidateIdentifier type:(IMKStyleType) theType;
```

## See Also

### Instance Methods
- [func candidateFrame() -> NSRect](./candidateframe%28%29.md)
- [func candidateIdentifier(atLineNumber: Int) -> Int](./candidateidentifier%28atlinenumber%29.md)
- [func candidateStringIdentifier(Any!) -> Int](./candidatestringidentifier%28_%29.md)
- [func clearSelection()](./clearselection%28%29.md)
- [func detachChild(Int)](./detachchild%28_%29.md)
- [func hideChild()](./hidechild%28%29.md)
- [func lineNumberForCandidate(withIdentifier: Int) -> Int](./linenumberforcandidate%28withidentifier%29.md)
- [func selectCandidate(Int)](./selectcandidate%28_%29.md)
- [func selectCandidate(withIdentifier: Int) -> Bool](./selectcandidate%28withidentifier%29.md)
- [func selectedCandidate() -> Int](./selectedcandidate%28%29.md)
- [func selectedCandidateString() -> NSAttributedString!](./selectedcandidatestring%28%29.md)
- [func setCandidateData([Any]!)](./setcandidatedata%28_%29.md)
- [func setCandidateFrameTopLeft(NSPoint)](./setcandidateframetopleft%28_%29.md)
- [func show()](./show%28%29.md)
- [func showChild()](./showchild%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/attachchild(_:tocandidate:type:))*