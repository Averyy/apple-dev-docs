# NSTextCheckingController

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NSTextCheckingController
```

```objc
@interface NSTextCheckingController : NSObject
```

## Topics

### Initializers
- [init(client: any NSTextCheckingClient)](./nstextcheckingcontroller/init%28client%29.md)
### Instance Properties
- [var client: any NSTextCheckingClient](./nstextcheckingcontroller/client.md)
- [var spellCheckerDocumentTag: Int](./nstextcheckingcontroller/spellcheckerdocumenttag.md)
### Instance Methods
- [func changeSpelling(Any?)](./nstextcheckingcontroller/changespelling%28_%29.md)
- [func checkSpelling(Any?)](./nstextcheckingcontroller/checkspelling%28_%29.md)
- [func checkText(in: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any])](./nstextcheckingcontroller/checktext%28in,types,options%29.md)
- [func checkTextInDocument(Any?)](./nstextcheckingcontroller/checktextindocument%28_%29.md)
- [func checkTextInSelection(Any?)](./nstextcheckingcontroller/checktextinselection%28_%29.md)
- [func considerTextChecking(for: NSRange)](./nstextcheckingcontroller/considertextchecking%28for%29.md)
- [func didChangeSelectedRange()](./nstextcheckingcontroller/didchangeselectedrange%28%29.md)
- [func didChangeText(in: NSRange)](./nstextcheckingcontroller/didchangetext%28in%29.md)
- [func ignoreSpelling(Any?)](./nstextcheckingcontroller/ignorespelling%28_%29.md)
- [func insertedText(in: NSRange)](./nstextcheckingcontroller/insertedtext%28in%29.md)
- [func invalidate()](./nstextcheckingcontroller/invalidate%28%29.md)
- [func menu(at: Int, clickedOnSelection: Bool, effectiveRange: NSRangePointer) -> NSMenu?](./nstextcheckingcontroller/menu%28at,clickedonselection,effectiverange%29.md)
- [func orderFrontSubstitutionsPanel(Any?)](./nstextcheckingcontroller/orderfrontsubstitutionspanel%28_%29.md)
- [func showGuessPanel(Any?)](./nstextcheckingcontroller/showguesspanel%28_%29.md)
- [func updateCandidates()](./nstextcheckingcontroller/updatecandidates%28%29.md)
- [func validAnnotations() -> [NSAttributedString.Key]](./nstextcheckingcontroller/validannotations%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text-checking
- [protocol NSTextCheckingClient](./nstextcheckingclient.md)
- [protocol NSTextInputTraits](./nstextinputtraits.md)
- [enum NSTextInputTraitType](./nstextinputtraittype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcheckingcontroller)*