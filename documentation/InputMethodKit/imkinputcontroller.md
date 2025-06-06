# IMKInputController

**Framework**: InputMethodKit  
**Kind**: class

The `IMKInputController` class provides a base class for custom input controller classes. The [`IMKServer`](imkserver.md)  class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding `IMKInputController` object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IMKInputController
```

#### Overview

An `IMKInputController` object controls text input on the input method side. It manages events and text from the applications and converted text from the input method engine. `IMKInputController` implements fully the [`IMKStateSetting`](imkstatesetting.md) and [`IMKMouseHandling`](imkmousehandling.md) protocols.  Typically you do not need to override this class, but you do need to provide  a delegate object that implements the methods that your are interested in.  The `IMKInputController` versions of the protocol methods check whether the delegate object implements a method, and  calls the delegate version if it exists.

## Topics

### Initializing an Input Controller
- [init!(server: IMKServer!, delegate: Any!, client: Any!)](imkinputcontroller/init(server:delegate:client:).md)
  Initializes the input control by setting the delegate.
### Working with Ranges
- [func compositionAttributes(at: NSRange) -> NSMutableDictionary!](imkinputcontroller/compositionattributes(at:).md)
  Returns a dictionary of text attributes.
- [func selectionRange() -> NSRange](imkinputcontroller/selectionrange.md)
  Returns where the range of the selection that should be placed inside marked text.
- [func replacementRange() -> NSRange](imkinputcontroller/replacementrange.md)
  Returns the range in the client document that the text should replace.
- [func mark(forStyle: Int, at: NSRange) -> [AnyHashable : Any]!](imkinputcontroller/mark(forstyle:at:).md)
  Returns a dictionary of text attributes that can mark a range of an attributed string to send to a client.
### Managing the Delegate
- [func delegate() -> Any!](imkinputcontroller/delegate.md)
  Returns the delegate for input controller  object.
- [func setDelegate(Any!)](imkinputcontroller/setdelegate(_:).md)
  Sets the delegate for input controller  object.
### Getting the Client and Server Objects
- [func server() -> IMKServer!](imkinputcontroller/server.md)
  Returns the server object that manages the input controller.
- [func client() -> (any IMKTextInput & NSObjectProtocol)!](imkinputcontroller/client.md)
  Returns the client object associated with the input controller.
### Tracking Selections
- [func annotationSelected(NSAttributedString!, forCandidate: NSAttributedString!)](imkinputcontroller/annotationselected(_:forcandidate:).md)
  Sends the selected candidate string and annotation string to the input controller.
- [func candidateSelectionChanged(NSAttributedString!)](imkinputcontroller/candidateselectionchanged(_:).md)
  Informs an input controller that the current candidate selection in the candidate window has changed.
- [func candidateSelected(NSAttributedString!)](imkinputcontroller/candidateselected(_:).md)
  Informs an input controller that a new candidate is selected.
### Managing Composition
- [func updateComposition()](imkinputcontroller/updatecomposition.md)
  Informs the input controller that the composition has changed.
- [func cancelComposition()](imkinputcontroller/cancelcomposition.md)
  Stops the current composition and replaces marked text with the original text.
### Hiding the User Interface
- [func hidePalettes()](imkinputcontroller/hidepalettes.md)
  Informs an input method that it should  close any visible user interface.
### Working with Custom Commands
- [func doCommand(by: Selector!, command: [AnyHashable : Any]!)](imkinputcontroller/docommand(by:command:).md)
  Passes commands that are not generated as part of the text input process.
- [func menu() -> NSMenu!](imkinputcontroller/menu.md)
  Returns a menu of commands that are specific to an input method.
### Instance Methods
- [func inputControllerWillClose()](imkinputcontroller/inputcontrollerwillclose.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IMKMouseHandling](imkmousehandling.md)
- [IMKStateSetting](imkstatesetting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IMKCandidates](imkcandidates.md)
  The `IMKCandidates` class presents candidates to users and notifies the appropriate [`IMKInputController`](imkinputcontroller.md) object when the user selects a candidate.  are alternate characters for a given input sequence. The `IMKCandidates` class supports using a candidates window  in your input method; using `IMKCandidates` is optional. Not all input methods require them.
- [class IMKServer](imkserver.md)
  The `IMKServer` class manages client connections to your input method.  When you write the main function for your input method, you create an `IMKServer` object.  You should never need to override this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller)*