# IMKServer

**Framework**: InputMethodKit  
**Kind**: class

The `IMKServer` class manages client connections to your input method.  When you write the main function for your input method, you create an `IMKServer` object.  You should never need to override this class.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IMKServer
```

## Topics

### Initializing a Server Object
- [init!(name: String!, bundleIdentifier: String!)](imkserver/init(name:bundleidentifier:).md)
  Creates and returns a server object from property list information contained in the provided bundle.
- [init!(name: String!, controllerClass: AnyClass!, delegateClass: AnyClass!)](imkserver/init(name:controllerclass:delegateclass:).md)
  Creates and returns a server object initialized with the provided parameters.
### Getting a Bundle for the Input Method
- [func bundle() -> Bundle!](imkserver/bundle.md)
  Returns an `NSBundle` object for the input method.
### Constants
- [IMKModeDictionary](imkmodedictionary.md)
  The input method mode dictionary key.
- [IMKControllerClass](imkcontrollerclass.md)
  The input method controller class key.
- [IMKDelegateClass](imkdelegateclass.md)
  The input method delegate class key.
### Instance Methods
- [func lastKeyEventWasDeadKey() -> Bool](imkserver/lastkeyeventwasdeadkey.md)
- [func paletteWillTerminate() -> Bool](imkserver/palettewillterminate.md)

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

- [class IMKCandidates](imkcandidates.md)
  The `IMKCandidates` class presents candidates to users and notifies the appropriate [`IMKInputController`](imkinputcontroller.md) object when the user selects a candidate.  are alternate characters for a given input sequence. The `IMKCandidates` class supports using a candidates window  in your input method; using `IMKCandidates` is optional. Not all input methods require them.
- [class IMKInputController](imkinputcontroller.md)
  The `IMKInputController` class provides a base class for custom input controller classes. The [`IMKServer`](imkserver.md)  class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding `IMKInputController` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkserver)*