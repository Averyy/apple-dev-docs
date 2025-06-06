# NSTextCheckingController

**Framework**: AppKit  
**Kind**: class

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NSTextCheckingController
```

## Topics

### Initializers
- [init(client: any NSTextCheckingClient)](nstextcheckingcontroller/init(client:).md)
### Instance Properties
- [var client: any NSTextCheckingClient](nstextcheckingcontroller/client.md)
- [var spellCheckerDocumentTag: Int](nstextcheckingcontroller/spellcheckerdocumenttag.md)
### Instance Methods
- [func changeSpelling(Any?)](nstextcheckingcontroller/changespelling(_:).md)
- [func checkSpelling(Any?)](nstextcheckingcontroller/checkspelling(_:).md)
- [func checkText(in: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any])](nstextcheckingcontroller/checktext(in:types:options:).md)
- [func checkTextInDocument(Any?)](nstextcheckingcontroller/checktextindocument(_:).md)
- [func checkTextInSelection(Any?)](nstextcheckingcontroller/checktextinselection(_:).md)
- [func considerTextChecking(for: NSRange)](nstextcheckingcontroller/considertextchecking(for:).md)
- [func didChangeSelectedRange()](nstextcheckingcontroller/didchangeselectedrange.md)
- [func didChangeText(in: NSRange)](nstextcheckingcontroller/didchangetext(in:).md)
- [func ignoreSpelling(Any?)](nstextcheckingcontroller/ignorespelling(_:).md)
- [func insertedText(in: NSRange)](nstextcheckingcontroller/insertedtext(in:).md)
- [func invalidate()](nstextcheckingcontroller/invalidate.md)
- [func menu(at: Int, clickedOnSelection: Bool, effectiveRange: NSRangePointer) -> NSMenu?](nstextcheckingcontroller/menu(at:clickedonselection:effectiverange:).md)
- [func orderFrontSubstitutionsPanel(Any?)](nstextcheckingcontroller/orderfrontsubstitutionspanel(_:).md)
- [func showGuessPanel(Any?)](nstextcheckingcontroller/showguesspanel(_:).md)
- [func updateCandidates()](nstextcheckingcontroller/updatecandidates.md)
- [func validAnnotations() -> [NSAttributedString.Key]](nstextcheckingcontroller/validannotations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSTextCheckingClient](nstextcheckingclient.md)
- [protocol NSTextInputTraits](nstextinputtraits.md)
- [enum NSTextInputTraitType](nstextinputtraittype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcheckingcontroller)*