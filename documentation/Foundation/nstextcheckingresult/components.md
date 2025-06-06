# components

**Framework**: Foundation  
**Kind**: property

A dictionary containing the components of a type checking result.

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
var components: [NSTextCheckingKey : String]? { get }
```

#### Discussion

Currently used by the transit checking result. The supported keys are located in [`Keys for Transit Components`](keys-for-transit-components.md).

## See Also

- [class func transitInformationCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult](nstextcheckingresult/transitinformationcheckingresult(range:components:).md)
  Creates and returns a text checking result with the specified transit information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/components)*