# addressComponents

**Framework**: Foundation  
**Kind**: property

The address dictionary of a type checking result.

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
var addressComponents: [NSTextCheckingKey : String]? { get }
```

#### Discussion

The dictionary keys are described in [`Keys for Address Components`](keys-for-address-components.md).

## See Also

- [class func addressCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult](nstextcheckingresult/addresscheckingresult(range:components:).md)
  Creates and returns a text checking result with the specified address components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/addresscomponents)*