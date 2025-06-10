# always(includingZero:)

**Framework**: Foundation  
**Kind**: method

A strategy to always display sign symbols.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func always(includingZero: Bool = true) -> NumberFormatStyleConfiguration.SignDisplayStrategy
```

#### Return Value

A strategy to always display sign symbols, with the given behavior for zero values.

## Parameters

- `includingZero`: A Boolean value that determines whether the format style should apply sign characters to zero values. Defaults to  .

## See Also

- [static var automatic: NumberFormatStyleConfiguration.SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy/automatic.md)
  A strategy to automatically configure locale-appropriate sign display behavior.
- [static var never: NumberFormatStyleConfiguration.SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy/never.md)
  A strategy to never display sign symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy/always(includingzero:))*