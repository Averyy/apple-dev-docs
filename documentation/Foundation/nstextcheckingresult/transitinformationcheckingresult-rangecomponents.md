# transitInformationCheckingResult(range:components:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result with the specified transit information.

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
class func transitInformationCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`transitInformation`](nstextcheckingresult/checkingtype/transitinformation.md).

## Parameters

- `range`: The range of the detected result.
- `components`: A dictionary containing the transit components. The currently supported keys are   and  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/transitinformationcheckingresult(range:components:))*