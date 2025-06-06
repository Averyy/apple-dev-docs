# IMKCandidates

**Framework**: InputMethodKit  
**Kind**: class

The `IMKCandidates` class presents candidates to users and notifies the appropriate [`IMKInputController`](imkinputcontroller.md) object when the user selects a candidate.  are alternate characters for a given input sequence. The `IMKCandidates` class supports using a candidates window  in your input method; using `IMKCandidates` is optional. Not all input methods require them.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class IMKCandidates
```

#### Overview

When you create an `IMKCandidates` object, you attach it to the `IMKServer` object for your input method.  You then need to override the `IMKInputController` methods `candidateSelectionChanged:` and `candidateSelected:` as well as implement a candidates method in your delegate object.  The `IMKInputController` subclass supplies candidates to the `IMKCandidates` object by implementing the candidates method. When you are ready to display a candidates window, call the candidates method to update candidates and to show the candidates window.

## Topics

### Initializing a Candidates Window
- [init!(server: IMKServer!, panelType: IMKCandidatePanelType)](imkcandidates/init(server:paneltype:).md)
  Returns the initialized `IMKCandidates` object.
### Managing Selection Keys
- [func setSelectionKeys([Any]!)](imkcandidates/setselectionkeys(_:).md)
  Sets the selection keys for the candidates.
- [func selectionKeys() -> [Any]!](imkcandidates/selectionkeys.md)
  Returns an array of `NSNumber` objects where each `NSNumber` object represents a virtual key code.
- [func setSelectionKeysKeylayout(TISInputSource!)](imkcandidates/setselectionkeyskeylayout(_:).md)
  Sets the key layout that is used to map virtual key codes to characters.
- [func selectionKeysKeylayout() -> Unmanaged<TISInputSource>!](imkcandidates/selectionkeyskeylayout.md)
  Returns the key layout that maps virtual key codes to selection keys.
### Managing Window Visibility and Behavior
- [func show(IMKCandidatesLocationHint)](imkcandidates/show(_:).md)
  Shows the candidates window.
- [func hide()](imkcandidates/hide.md)
  Hides a candidates window, if it is visible.
- [func isVisible() -> Bool](imkcandidates/isvisible.md)
  Returns whether or not the candidates window is visible.
- [func setDismissesAutomatically(Bool)](imkcandidates/setdismissesautomatically(_:).md)
  Sets the state of the flag that determines whether the candidates window dismisses automatically.
- [func dismissesAutomatically() -> Bool](imkcandidates/dismissesautomatically.md)
  Returns the state of the flag that determines whether the candidates window dismisses automatically.
- [func update()](imkcandidates/update.md)
  Updates the candidates that are displayed in the candidates window.
### Managing Window Type and Text Attributes
- [func panelType() -> IMKCandidatePanelType](imkcandidates/paneltype.md)
  Returns the style of the candidates window.
- [func setPanelType(IMKCandidatePanelType)](imkcandidates/setpaneltype(_:).md)
  Sets the style of the candidates window.
- [func setAttributes([AnyHashable : Any]!)](imkcandidates/setattributes(_:).md)
  Sets the style attributes for the candidates window.
- [func attributes() -> [AnyHashable : Any]!](imkcandidates/attributes.md)
  Returns a dictionary of the style attributes used for the candidates window..
### Showing an Annotation Window
- [func showAnnotation(NSAttributedString!)](imkcandidates/showannotation(_:).md)
  Displays an annotation string in an annotation window.
### Constants
- [typealias IMKCandidatePanelType](imkcandidatepaneltype.md)
  Types of candidates windows provide by the Input Method Kit.
- [typealias IMKCandidatesLocationHint](imkcandidateslocationhint.md)
  Hints that suggest where to place the candidates window.
- [IMKCandidatesOpacityAttributeName](imkcandidatesopacityattributename.md)
  The opacity level for a candidates window.
### Initializers
- [init!(server: IMKServer!, panelType: IMKCandidatePanelType, styleType: IMKStyleType)](imkcandidates/init(server:paneltype:styletype:).md)
### Instance Methods
- [func attachChild(IMKCandidates!, toCandidate: Int, type: IMKStyleType)](imkcandidates/attachchild(_:tocandidate:type:).md)
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
- [func showSublist([Any]!, subListDelegate: Any!)](imkcandidates/showsublist(_:sublistdelegate:).md)

## Relationships

### Inherits From
- [NSResponder](../AppKit/NSResponder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)

## See Also

- [class IMKInputController](imkinputcontroller.md)
  The `IMKInputController` class provides a base class for custom input controller classes. The [`IMKServer`](imkserver.md)  class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding `IMKInputController` object.
- [class IMKServer](imkserver.md)
  The `IMKServer` class manages client connections to your input method.  When you write the main function for your input method, you create an `IMKServer` object.  You should never need to override this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates)*