# checkingTypes

**Framework**: Foundation  
**Kind**: property

Returns the checking types for the data detector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var checkingTypes: NSTextCheckingTypes { get }
```

#### Discussion

The supported subset of checking types are specified in [`NSTextCheckingResult.CheckingType`](nstextcheckingresult/checkingtype.md). Those constants can be combined using the C-bitwise OR operator.

Currently, the supported data detectors `checkingTypes` are:  [`date`](nstextcheckingresult/checkingtype/date.md), [`address`](nstextcheckingresult/checkingtype/address.md), [`link`](nstextcheckingresult/checkingtype/link.md), `NSTextCheckingTypePhoneNumber`, and `NSTextCheckingTypeTransitInformation`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatadetector/checkingtypes)*