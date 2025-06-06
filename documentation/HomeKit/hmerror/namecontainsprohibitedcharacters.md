# nameContainsProhibitedCharacters

**Framework**: HomeKit  
**Kind**: property

An attempt to name an object with prohibited characters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var nameContainsProhibitedCharacters: HMError.Code { get }
```

#### Discussion

Only letters, symbols, numbers, spaces, and apostrophes are permitted in names.

## See Also

- [static var invalidDataFormatSpecified: HMError.Code](hmerror/invaliddataformatspecified.md)
  An error indicating an invalid data format was specified.
- [static var invalidValueType: HMError.Code](hmerror/invalidvaluetype.md)
  An attempt to use an invalid value type.
- [static var nameDoesNotEndWithValidCharacters: HMError.Code](hmerror/namedoesnotendwithvalidcharacters.md)
  An error indicating the provided name has invalid characters at the end.
- [static var nameDoesNotStartWithValidCharacters: HMError.Code](hmerror/namedoesnotstartwithvalidcharacters.md)
  An attempt to start the name of an object with invalid characters.
- [static var stringLongerThanMaximum: HMError.Code](hmerror/stringlongerthanmaximum.md)
  An attempt to use a string longer than the maximum allowed.
- [static var stringShorterThanMinimum: HMError.Code](hmerror/stringshorterthanminimum.md)
  An attempt to use a string shorter than the required minimum.
- [static var valueHigherThanMaximum: HMError.Code](hmerror/valuehigherthanmaximum.md)
  An attempt to use a numeric value higher than the specified maximum value.
- [static var valueLowerThanMinimum: HMError.Code](hmerror/valuelowerthanminimum.md)
  An attempt to use a numeric value lower than the specified minimum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/namecontainsprohibitedcharacters)*