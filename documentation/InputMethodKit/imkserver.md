# IMKServer

**Framework**: InputMethodKit  
**Kind**: class  
**Role**: Class

The `IMKServer` class manages client connections to your input method.  When you write the main function for your input method, you create an `IMKServer` object.  You should never need to override this class.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IMKServer
```

```objc
@interface IMKServer : NSObject
```

## Topics

### Initializing a Server Object
- [init!(name: String!, bundleIdentifier: String!)](./imkserver/init%28name,bundleidentifier%29.md)
  Creates and returns a server object from property list information contained in the provided bundle.
- [init!(name: String!, controllerClass: AnyClass!, delegateClass: AnyClass!)](./imkserver/init%28name,controllerclass,delegateclass%29.md)
  Creates and returns a server object initialized with the provided parameters.
### Getting a Bundle for the Input Method
- [func bundle() -> Bundle!](./imkserver/bundle%28%29.md)
  Returns an `NSBundle` object for the input method.
### Instance Methods
- [func lastKeyEventWasDeadKey() -> Bool](./imkserver/lastkeyeventwasdeadkey%28%29.md)
- [func paletteWillTerminate() -> Bool](./imkserver/palettewillterminate%28%29.md)

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

### Classes
- [class IMKCandidates](./imkcandidates.md)
  The `IMKCandidates` class presents candidates to users and notifies the appropriate [`IMKInputController`](./imkinputcontroller.md) object when the user selects a candidate. **Candidates** are alternate characters for a given input sequence. The `IMKCandidates` class supports using a candidates window  in your input method; using `IMKCandidates` is optional. Not all input methods require them.
- [class IMKInputController](./imkinputcontroller.md)
  The `IMKInputController` class provides a base class for custom input controller classes. The [`IMKServer`](./imkserver.md)  class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding `IMKInputController` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkserver)*