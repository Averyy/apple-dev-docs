# NSTextCheckingResult.CheckingType

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

These constants specify the type of checking the methods should do. They are returned by [`resultType`](./resulttype.md).

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

```c
enum NSTextCheckingType : uint64_t;
```

## Topics

### Constants
- [static var orthography: NSTextCheckingResult.CheckingType](./checkingtype/orthography.md)
  Attempts to identify the language
- [static var spelling: NSTextCheckingResult.CheckingType](./checkingtype/spelling.md)
  Checks spelling.
- [static var grammar: NSTextCheckingResult.CheckingType](./checkingtype/grammar.md)
  Checks grammar.
- [static var date: NSTextCheckingResult.CheckingType](./checkingtype/date.md)
  Attempts to locate dates.
- [static var address: NSTextCheckingResult.CheckingType](./checkingtype/address.md)
  Attempts to locate addresses.
- [static var link: NSTextCheckingResult.CheckingType](./checkingtype/link.md)
  Attempts to locate URL links.
- [static var quote: NSTextCheckingResult.CheckingType](./checkingtype/quote.md)
  Replaces quotes with smart quotes.
- [static var dash: NSTextCheckingResult.CheckingType](./checkingtype/dash.md)
  Replaces dashes with em-dashes.
- [static var replacement: NSTextCheckingResult.CheckingType](./checkingtype/replacement.md)
  Replaces characters such as (c) with the appropriate symbol (in this case ©).
- [static var correction: NSTextCheckingResult.CheckingType](./checkingtype/correction.md)
  Performs autocorrection on misspelled words.
- [static var regularExpression: NSTextCheckingResult.CheckingType](./checkingtype/regularexpression.md)
  Matches a regular expression.
- [static var phoneNumber: NSTextCheckingResult.CheckingType](./checkingtype/phonenumber.md)
  Matches a phone number.
- [static var transitInformation: NSTextCheckingResult.CheckingType](./checkingtype/transitinformation.md)
  Matches a transit information, for example, flight information.
### Initializers
- [init(rawValue: UInt64)](./checkingtype/init%28rawvalue%29.md)
### Type Properties
- [static var allCustomTypes: NSTextCheckingResult.CheckingType](./checkingtype/allcustomtypes.md)
- [static var allSystemTypes: NSTextCheckingResult.CheckingType](./checkingtype/allsystemtypes.md)
- [static var allTypes: NSTextCheckingResult.CheckingType](./checkingtype/alltypes.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [Keys for Transit Components](../keys-for-transit-components.md)
  The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](../keys-for-address-components.md)
  The following constants identify the possible keys returned in the [`addressComponents`](./addresscomponents.md) dictionary.
- [typealias NSTextCheckingTypes](../nstextcheckingtypes.md)
  Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.
- [struct NSTextCheckingKey](../nstextcheckingkey.md)
- [Anonymous](../api-1476845-anonymous.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype)*