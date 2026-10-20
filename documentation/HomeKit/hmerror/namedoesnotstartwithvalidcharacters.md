# nameDoesNotStartWithValidCharacters

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An attempt to start the name of an object with invalid characters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var nameDoesNotStartWithValidCharacters: HMError.Code { get }
```

#### Discussion

Names must start with a letter, symbol, or number.

## See Also

### Detecting value errors
- [static var invalidDataFormatSpecified: HMError.Code](./invaliddataformatspecified.md)
  An error indicating an invalid data format was specified.
- [static var invalidValueType: HMError.Code](./invalidvaluetype.md)
  An attempt to use an invalid value type.
- [static var nameContainsProhibitedCharacters: HMError.Code](./namecontainsprohibitedcharacters.md)
  An attempt to name an object with prohibited characters.
- [static var nameDoesNotEndWithValidCharacters: HMError.Code](./namedoesnotendwithvalidcharacters.md)
  An error indicating the provided name has invalid characters at the end.
- [static var stringLongerThanMaximum: HMError.Code](./stringlongerthanmaximum.md)
  An attempt to use a string longer than the maximum allowed.
- [static var stringShorterThanMinimum: HMError.Code](./stringshorterthanminimum.md)
  An attempt to use a string shorter than the required minimum.
- [static var valueHigherThanMaximum: HMError.Code](./valuehigherthanmaximum.md)
  An attempt to use a numeric value higher than the specified maximum value.
- [static var valueLowerThanMinimum: HMError.Code](./valuelowerthanminimum.md)
  An attempt to use a numeric value lower than the specified minimum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/namedoesnotstartwithvalidcharacters)*