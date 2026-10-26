# dataDetectorWithTypes:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a new data detector instance.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSDataDetector *) dataDetectorWithTypes:(NSTextCheckingTypes) checkingTypes error:(NSError **) error;
```

#### Return Value

Returns the newly initialized data detector. If an error was encountered returns `nil`, and `error` contains the error.

#### Discussion

Currently, the supported data detectors `checkingTypes` are:  [`date`](../nstextcheckingresult/checkingtype/date.md), [`address`](../nstextcheckingresult/checkingtype/address.md), [`link`](../nstextcheckingresult/checkingtype/link.md), `NSTextCheckingTypePhoneNumber`, and `NSTextCheckingTypeTransitInformation`.

## Parameters

- `checkingTypes`: The checking types. The supported checking types are a subset of the types specified in [`NSTextCheckingResult.CheckingType`](../nstextcheckingresult/checkingtype.md). Those constants can be combined using the C-bitwise OR operator.
- `error`: An out parameter that if an error occurs during initialization contains the encountered error.

## See Also

### Related Documentation
- [var checkingTypes: NSTextCheckingTypes](./checkingtypes.md)
  Returns the checking types for the data detector.
### Creating data detector instances
- [init(types: NSTextCheckingTypes) throws](./init%28types%29.md)
  Initializes and returns a data detector instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatadetector/datadetectorwithtypes:error:)*