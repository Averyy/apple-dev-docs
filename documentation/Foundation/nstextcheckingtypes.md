# NSTextCheckingTypes

**Framework**: Foundation  
**Kind**: typealias

Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.

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
typealias NSTextCheckingTypes = UInt64
```

## Topics

### Constants
- [var NSTextCheckingAllSystemTypes: NSTextCheckingTypes](nstextcheckingallsystemtypes.md)
  Checking types supported by the system. The first 32 types are reserved.
- [var NSTextCheckingAllCustomTypes: NSTextCheckingTypes](nstextcheckingallcustomtypes.md)
  Checking types that can be used by clients.
- [var NSTextCheckingAllTypes: NSTextCheckingTypes](nstextcheckingalltypes.md)
  All possible checking types, both system- and user-supported.

## See Also

- [Keys for Transit Components](keys-for-transit-components.md)
  The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](keys-for-address-components.md)
  The following constants identify the possible keys returned in the [`addressComponents`](nstextcheckingresult/addresscomponents.md) dictionary.
- [NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype.md)
  These constants specify the type of checking the methods should do. They are returned by [`resultType`](nstextcheckingresult/resulttype.md).
- [struct NSTextCheckingKey](nstextcheckingkey.md)
- [Anonymous](1476845-anonymous.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingtypes)*