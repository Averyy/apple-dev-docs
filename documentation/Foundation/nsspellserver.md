# NSSpellServer

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A server that your app uses to provide a spell checker service to other apps running in the system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSSpellServer
```

```objc
@interface NSSpellServer : NSObject
```

## Overview

A **service provider** is an application that declares its availability in a standard way, so that any other applications that wish to use it can do so. If you build a spelling checker that makes use of the [`NSSpellServer`](./nsspellserver.md) class and list it as an available service, then users of any application that makes use of [`NSSpellChecker`](../AppKit/nsspellchecker.md) or includes a Services menu will see your spelling checker as one of the available dictionaries.

## Topics

### Configuring Spelling Servers
- [var delegate: (any NSSpellServerDelegate)?](./nsspellserver/delegate.md)
  Returns the receiver’s delegate.
### Providing Spelling Services
- [func registerLanguage(String?, byVendor: String?) -> Bool](./nsspellserver/registerlanguage%28_,byvendor%29.md)
  Notifies the receiver of a language your spelling checker can check.
- [func run()](./nsspellserver/run%28%29.md)
  Causes the receiver to start listening for spell-checking requests.
### Managing the Spell-Checking Process
- [func isWord(inUserDictionaries: String, caseSensitive: Bool) -> Bool](./nsspellserver/isword%28inuserdictionaries,casesensitive%29.md)
  Indicates whether a given word is in the user’s list of learned words or the document’s list of words to ignore.
### Constants
- [Grammatical-Analysis Details](./grammatical-analysis-details.md)
  These constants are used as the keys in the outDetails dictionaries returned by [`NSSpellServer`](./nsspellserver.md) and [`checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)`](../AppKit/nsspellchecker/checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md) ([`NSSpellChecker`](../AppKit/nsspellchecker.md)).

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

### Spelling and Grammar
- [protocol NSSpellServerDelegate](./nsspellserverdelegate.md)
  The optional methods implemented by the delegate of a spell server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserver)*