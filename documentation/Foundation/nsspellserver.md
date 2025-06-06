# NSSpellServer

**Framework**: Foundation  
**Kind**: class

A server that your app uses to provide a spell checker service to other apps running in the system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSSpellServer
```

#### Overview

A  is an application that declares its availability in a standard way, so that any other applications that wish to use it can do so. If you build a spelling checker that makes use of the [`NSSpellServer`](nsspellserver.md) class and list it as an available service, then users of any application that makes use of [`NSSpellChecker`](https://developer.apple.com/documentation/AppKit/NSSpellChecker) or includes a Services menu will see your spelling checker as one of the available dictionaries.

## Topics

### Configuring Spelling Servers
- [var delegate: (any NSSpellServerDelegate)?](nsspellserver/delegate.md)
  Returns the receiver’s delegate.
### Providing Spelling Services
- [func registerLanguage(String?, byVendor: String?) -> Bool](nsspellserver/registerlanguage(_:byvendor:).md)
  Notifies the receiver of a language your spelling checker can check.
- [func run()](nsspellserver/run.md)
  Causes the receiver to start listening for spell-checking requests.
### Managing the Spell-Checking Process
- [func isWord(inUserDictionaries: String, caseSensitive: Bool) -> Bool](nsspellserver/isword(inuserdictionaries:casesensitive:).md)
  Indicates whether a given word is in the user’s list of learned words or the document’s list of words to ignore.
### Constants
- [Grammatical-Analysis Details](grammatical-analysis-details.md)
  These constants are used as the keys in the outDetails dictionaries returned by [`NSSpellServer`](nsspellserver.md) and [`checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)`](https://developer.apple.com/documentation/AppKit/NSSpellChecker/checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)) ([`NSSpellChecker`](https://developer.apple.com/documentation/AppKit/NSSpellChecker)).

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

- [protocol NSSpellServerDelegate](nsspellserverdelegate.md)
  The optional methods implemented by the delegate of a spell server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserver)*