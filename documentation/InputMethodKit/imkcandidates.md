# IMKCandidates

**Framework**: InputMethodKit  
**Kind**: class  
**Role**: Class

The `IMKCandidates` class presents candidates to users and notifies the appropriate [`IMKInputController`](./imkinputcontroller.md) object when the user selects a candidate. **Candidates** are alternate characters for a given input sequence. The `IMKCandidates` class supports using a candidates window  in your input method; using `IMKCandidates` is optional. Not all input methods require them.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IMKCandidates
```

```objc
@interface IMKCandidates : NSResponder
```

#### Overview

When you create an `IMKCandidates` object, you attach it to the `IMKServer` object for your input method.  You then need to override the `IMKInputController` methods `candidateSelectionChanged:` and `candidateSelected:` as well as implement a candidates method in your delegate object.  The `IMKInputController` subclass supplies candidates to the `IMKCandidates` object by implementing the candidates method. When you are ready to display a candidates window, call the candidates method to update candidates and to show the candidates window.

## Topics

### Initializing a Candidates Window
- [init!(server: IMKServer!, panelType: IMKCandidatePanelType)](./imkcandidates/init%28server,paneltype%29.md)
  Returns the initialized `IMKCandidates` object.
### Managing Selection Keys
- [func setSelectionKeys([Any]!)](./imkcandidates/setselectionkeys%28_%29.md)
  Sets the selection keys for the candidates.
- [func selectionKeys() -> [Any]!](./imkcandidates/selectionkeys%28%29.md)
  Returns an array of `NSNumber` objects where each `NSNumber` object represents a virtual key code.
- [func setSelectionKeysKeylayout(TISInputSource!)](./imkcandidates/setselectionkeyskeylayout%28_%29.md)
  Sets the key layout that is used to map virtual key codes to characters.
- [func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!](./imkcandidates/selectionkeyskeylayout%28%29.md)
  Returns the key layout that maps virtual key codes to selection keys.
### Managing Window Visibility and Behavior
- [func show(IMKCandidatesLocationHint)](./imkcandidates/show%28_%29.md)
  Shows the candidates window.
- [func hide()](./imkcandidates/hide%28%29.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](./imkcandidates/isvisible%28%29.md)
  Returns whether or not the candidates window is visible.
- [func setDismissesAutomatically(Bool)](./imkcandidates/setdismissesautomatically%28_%29.md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func dismissesAutomatically() -> Bool](./imkcandidates/dismissesautomatically%28%29.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](./imkcandidates/update%28%29.md)
  Updates the candidates that are displayed in the candidates window.
### Managing Window Type and Text Attributes
- [func panelType() -> IMKCandidatePanelType](./imkcandidates/paneltype%28%29.md)
  Returns the style of the candidates window.
- [func setPanelType(IMKCandidatePanelType)](./imkcandidates/setpaneltype%28_%29.md)
  Sets the style of the candidates window.
- [func setAttributes([AnyHashable : Any]!)](./imkcandidates/setattributes%28_%29.md)
  Sets the style attributes for the candidates window.
- [func attributes() -> [AnyHashable : Any]!](./imkcandidates/attributes%28%29.md)
  Returns a dictionary of the style attributes used for the candidates window..
### Showing an Annotation Window
- [func showAnnotation(NSAttributedString!)](./imkcandidates/showannotation%28_%29.md)
  Displays an annotation string in an annotation window.
### Constants
- [typealias IMKCandidatePanelType](./imkcandidatepaneltype.md)
  Types of candidates windows provide by the Input Method Kit.
- [typealias IMKCandidatesLocationHint](./imkcandidateslocationhint.md)
  Hints that suggest where to place the candidates window.
### Initializers
- [init!(server: IMKServer!, panelType: IMKCandidatePanelType, styleType: IMKStyleType)](./imkcandidates/init%28server,paneltype,styletype%29.md)
### Instance Methods
- [func attachChild(IMKCandidates!, toCandidate: Int, type: IMKStyleType)](./imkcandidates/attachchild%28_,tocandidate,type%29.md)
- [func candidateFrame() -> NSRect](./imkcandidates/candidateframe%28%29.md)
- [func candidateIdentifier(atLineNumber: Int) -> Int](./imkcandidates/candidateidentifier%28atlinenumber%29.md)
- [func candidateStringIdentifier(Any!) -> Int](./imkcandidates/candidatestringidentifier%28_%29.md)
- [func clearSelection()](./imkcandidates/clearselection%28%29.md)
- [func detachChild(Int)](./imkcandidates/detachchild%28_%29.md)
- [func hideChild()](./imkcandidates/hidechild%28%29.md)
- [func lineNumberForCandidate(withIdentifier: Int) -> Int](./imkcandidates/linenumberforcandidate%28withidentifier%29.md)
- [func selectCandidate(Int)](./imkcandidates/selectcandidate%28_%29.md)
- [func selectCandidate(withIdentifier: Int) -> Bool](./imkcandidates/selectcandidate%28withidentifier%29.md)
- [func selectedCandidate() -> Int](./imkcandidates/selectedcandidate%28%29.md)
- [func selectedCandidateString() -> NSAttributedString!](./imkcandidates/selectedcandidatestring%28%29.md)
- [func setCandidateData([Any]!)](./imkcandidates/setcandidatedata%28_%29.md)
- [func setCandidateFrameTopLeft(NSPoint)](./imkcandidates/setcandidateframetopleft%28_%29.md)
- [func show()](./imkcandidates/show%28%29.md)
- [func showChild()](./imkcandidates/showchild%28%29.md)
- [func showSublist([Any]!, subListDelegate: Any!)](./imkcandidates/showsublist%28_,sublistdelegate%29.md)

## Relationships

### Inherits From
- [NSResponder](../AppKit/nsresponder.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)

## See Also

### Classes
- [class IMKInputController](./imkinputcontroller.md)
  The `IMKInputController` class provides a base class for custom input controller classes. The [`IMKServer`](./imkserver.md)  class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding `IMKInputController` object.
- [class IMKServer](./imkserver.md)
  The `IMKServer` class manages client connections to your input method.  When you write the main function for your input method, you create an `IMKServer` object.  You should never need to override this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates)*