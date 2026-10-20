# correction

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Performs autocorrection on misspelled words.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var correction: NSTextCheckingResult.CheckingType { get }
```

```c
NSTextCheckingTypeCorrection
```

## See Also

### Constants
- [static var orthography: NSTextCheckingResult.CheckingType](./orthography.md)
  Attempts to identify the language
- [static var spelling: NSTextCheckingResult.CheckingType](./spelling.md)
  Checks spelling.
- [static var grammar: NSTextCheckingResult.CheckingType](./grammar.md)
  Checks grammar.
- [static var date: NSTextCheckingResult.CheckingType](./date.md)
  Attempts to locate dates.
- [static var address: NSTextCheckingResult.CheckingType](./address.md)
  Attempts to locate addresses.
- [static var link: NSTextCheckingResult.CheckingType](./link.md)
  Attempts to locate URL links.
- [static var quote: NSTextCheckingResult.CheckingType](./quote.md)
  Replaces quotes with smart quotes.
- [static var dash: NSTextCheckingResult.CheckingType](./dash.md)
  Replaces dashes with em-dashes.
- [static var replacement: NSTextCheckingResult.CheckingType](./replacement.md)
  Replaces characters such as (c) with the appropriate symbol (in this case ©).
- [static var regularExpression: NSTextCheckingResult.CheckingType](./regularexpression.md)
  Matches a regular expression.
- [static var phoneNumber: NSTextCheckingResult.CheckingType](./phonenumber.md)
  Matches a phone number.
- [static var transitInformation: NSTextCheckingResult.CheckingType](./transitinformation.md)
  Matches a transit information, for example, flight information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/correction)*