# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

Fits a transformer to a data frame

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func fitted(to input: DataFrame, validateOn validation: DataFrame?, eventHandler: EventHandler?) async throws -> Self.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A data frame containing examples used for fitting the transformer.
- `validation`: A data frame containing examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

- [func fitted(to: DataFrame, validateOn: DataFrame?) async throws -> Self.Transformer](supervisedtabularestimator/fitted(to:validateon:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator/fitted(to:validateon:eventhandler:))*