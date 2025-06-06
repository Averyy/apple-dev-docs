# InputMethodKit

**Framework**: InputMethodKit  
**Kind**: module

Develop input methods and manage communication with client applications, candidates windows, and input method modes.

**Availability**:
- macOS 10.5+

#### Overview

The Input Method Kit, introduced in OS X v10.5, provides a streamlined programming interface that lets you develop input methods with far less code than older Mac programming interfaces. It is fully integrated with the Text Services Manager. The Input Method Kit allows 32-bit applications to work with 64-bit applications.

The Input Method Kit provides classes and protocols for managing communication with client applications, candidates windows, and input method modes. Input methods supply text from a conversion engine (written in any language, such as C, C++, Objective-C, Python, and so on), key bindings and optional event handling, and information about your input method in an extended `Info.plist` file. You also have the option to provide menu items that support input-method-specific commands or preferences settings.

## Topics

### Classes
- [class IMKCandidates](imkcandidates.md)
  The `IMKCandidates` class presents candidates to users and notifies the appropriate [`IMKInputController`](imkinputcontroller.md) object when the user selects a candidate.  are alternate characters for a given input sequence. The `IMKCandidates` class supports using a candidates window  in your input method; using `IMKCandidates` is optional. Not all input methods require them.
- [class IMKInputController](imkinputcontroller.md)
  The `IMKInputController` class provides a base class for custom input controller classes. The [`IMKServer`](imkserver.md)  class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding `IMKInputController` object.
- [class IMKServer](imkserver.md)
  The `IMKServer` class manages client connections to your input method.  When you write the main function for your input method, you create an `IMKServer` object.  You should never need to override this class.
### Protocols
- [protocol IMKMouseHandling](imkmousehandling.md)
  The `IMKMouseHandling` protocol defines methods that your input method can implement to handle mouse events.
- [IMKServerInput](imkserverinput.md)
  `IMKServerInput` is an informal protocol that defines methods for receiving text events. This is intentionally not a formal protocol because there are three ways to receive events. An input method chooses one of the following approaches and implements the appropriate methods:
- [protocol IMKStateSetting](imkstatesetting.md)
  The `IMKStateSetting` protocol defines methods for setting or accessing values that indicate the state of an input method.
### Reference
- [InputMethodKit Enumerations](inputmethodkit-enumerations.md)
- [InputMethodKit Constants](inputmethodkit-constants.md)
- [InputMethodKit Data Types](inputmethodkit-data_types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/InputMethodKit)*