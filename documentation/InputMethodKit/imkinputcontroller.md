# IMKInputController

**Framework**: InputMethodKit  
**Kind**: class  
**Role**: Class

The `IMKInputController` class provides a base class for custom input controller classes. The [`IMKServer`](./imkserver.md)  class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding `IMKInputController` object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IMKInputController
```

```objc
@interface IMKInputController : NSObject
```

## Overview

An `IMKInputController` object controls text input on the input method side. It manages events and text from the applications and converted text from the input method engine. `IMKInputController` implements fully the [`IMKStateSetting`](./imkstatesetting.md) and [`IMKMouseHandling`](./imkmousehandling.md) protocols.  Typically you do not need to override this class, but you do need to provide  a delegate object that implements the methods that your are interested in.  The `IMKInputController` versions of the protocol methods check whether the delegate object implements a method, and  calls the delegate version if it exists.

## Topics

### Initializing an Input Controller
- [init!(server: IMKServer!, delegate: Any!, client: Any!)](./imkinputcontroller/init%28server,delegate,client%29.md)
  Initializes the input control by setting the delegate.
### Working with Ranges
- [func compositionAttributes(at: NSRange) -> NSMutableDictionary!](./imkinputcontroller/compositionattributes%28at%29.md)
  Returns a dictionary of text attributes.
- [func selectionRange() -> NSRange](./imkinputcontroller/selectionrange%28%29.md)
  Returns where the range of the selection that should be placed inside marked text.
- [func replacementRange() -> NSRange](./imkinputcontroller/replacementrange%28%29.md)
  Returns the range in the client document that the text should replace.
- [func mark(forStyle: Int, at: NSRange) -> [AnyHashable : Any]!](./imkinputcontroller/mark%28forstyle,at%29.md)
  Returns a dictionary of text attributes that can mark a range of an attributed string to send to a client.
### Managing the Delegate
- [func delegate() -> Any!](./imkinputcontroller/delegate%28%29.md)
  Returns the delegate for input controller  object.
- [func setDelegate(Any!)](./imkinputcontroller/setdelegate%28_%29.md)
  Sets the delegate for input controller  object.
### Getting the Client and Server Objects
- [func server() -> IMKServer!](./imkinputcontroller/server%28%29.md)
  Returns the server object that manages the input controller.
- [func client() -> (any IMKTextInput & NSObjectProtocol)!](./imkinputcontroller/client%28%29.md)
  Returns the client object associated with the input controller.
### Tracking Selections
- [func annotationSelected(NSAttributedString!, forCandidate: NSAttributedString!)](./imkinputcontroller/annotationselected%28_,forcandidate%29.md)
  Sends the selected candidate string and annotation string to the input controller.
- [func candidateSelectionChanged(NSAttributedString!)](./imkinputcontroller/candidateselectionchanged%28_%29.md)
  Informs an input controller that the current candidate selection in the candidate window has changed.
- [func candidateSelected(NSAttributedString!)](./imkinputcontroller/candidateselected%28_%29.md)
  Informs an input controller that a new candidate is selected.
### Managing Composition
- [func updateComposition()](./imkinputcontroller/updatecomposition%28%29.md)
  Informs the input controller that the composition has changed.
- [func cancelComposition()](./imkinputcontroller/cancelcomposition%28%29.md)
  Stops the current composition and replaces marked text with the original text.
### Hiding the User Interface
- [func hidePalettes()](./imkinputcontroller/hidepalettes%28%29.md)
  Informs an input method that it should  close any visible user interface.
### Working with Custom Commands
- [func doCommand(by: Selector!, command: [AnyHashable : Any]!)](./imkinputcontroller/docommand%28by,command%29.md)
  Passes commands that are not generated as part of the text input process.
- [func menu() -> NSMenu!](./imkinputcontroller/menu%28%29.md)
  Returns a menu of commands that are specific to an input method.
### Instance Methods
- [func inputControllerWillClose()](./imkinputcontroller/inputcontrollerwillclose%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [IMKMouseHandling](./imkmousehandling.md)
- [IMKStateSetting](./imkstatesetting.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class IMKCandidates](./imkcandidates.md)
  The `IMKCandidates` class presents candidates to users and notifies the appropriate [`IMKInputController`](./imkinputcontroller.md) object when the user selects a candidate. **Candidates** are alternate characters for a given input sequence. The `IMKCandidates` class supports using a candidates window  in your input method; using `IMKCandidates` is optional. Not all input methods require them.
- [class IMKServer](./imkserver.md)
  The `IMKServer` class manages client connections to your input method.  When you write the main function for your input method, you create an `IMKServer` object.  You should never need to override this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller)*