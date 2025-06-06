# NSTextCheckingResult.CheckingType

**Framework**: Foundation  
**Kind**: struct

These constants specify the type of checking the methods should do. They are returned by [`resultType`](nstextcheckingresult/resulttype.md).

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
struct CheckingType
```

## Topics

### Constants
- [static var orthography: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/orthography.md)
  Attempts to identify the language
- [static var spelling: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/spelling.md)
  Checks spelling.
- [static var grammar: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/grammar.md)
  Checks grammar.
- [static var date: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/date.md)
  Attempts to locate dates.
- [static var address: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/address.md)
  Attempts to locate addresses.
- [static var link: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/link.md)
  Attempts to locate URL links.
- [static var quote: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/quote.md)
  Replaces quotes with smart quotes.
- [static var dash: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/dash.md)
  Replaces dashes with em-dashes.
- [static var replacement: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/replacement.md)
  Replaces characters such as (c) with the appropriate symbol (in this case ©).
- [static var correction: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/correction.md)
  Performs autocorrection on misspelled words.
- [static var regularExpression: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/regularexpression.md)
  Matches a regular expression.
- [static var phoneNumber: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/phonenumber.md)
  Matches a phone number.
- [static var transitInformation: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/transitinformation.md)
  Matches a transit information, for example, flight information.
- [static var orthography: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/orthography.md)
  Attempts to identify the language
- [static var spelling: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/spelling.md)
  Checks spelling.
- [static var grammar: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/grammar.md)
  Checks grammar.
- [static var date: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/date.md)
  Attempts to locate dates.
- [static var address: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/address.md)
  Attempts to locate addresses.
- [static var link: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/link.md)
  Attempts to locate URL links.
- [static var quote: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/quote.md)
  Replaces quotes with smart quotes.
- [static var dash: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/dash.md)
  Replaces dashes with em-dashes.
- [static var replacement: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/replacement.md)
  Replaces characters such as (c) with the appropriate symbol (in this case ©).
- [static var correction: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/correction.md)
  Performs autocorrection on misspelled words.
- [static var regularExpression: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/regularexpression.md)
  Matches a regular expression.
- [static var phoneNumber: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/phonenumber.md)
  Matches a phone number.
- [static var transitInformation: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/transitinformation.md)
  Matches a transit information, for example, flight information.
### Initializers
- [init(rawValue: UInt64)](nstextcheckingresult/checkingtype/init(rawvalue:).md)
### Type Properties
- [static var allCustomTypes: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/allcustomtypes.md)
- [static var allSystemTypes: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/allsystemtypes.md)
- [static var allTypes: NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype/alltypes.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Keys for Transit Components](keys-for-transit-components.md)
  The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](keys-for-address-components.md)
  The following constants identify the possible keys returned in the [`addressComponents`](nstextcheckingresult/addresscomponents.md) dictionary.
- [typealias NSTextCheckingTypes](nstextcheckingtypes.md)
  Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.
- [struct NSTextCheckingKey](nstextcheckingkey.md)
- [Anonymous](1476845-anonymous.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype)*