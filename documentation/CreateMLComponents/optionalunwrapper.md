# OptionalUnwrapper

**Framework**: Create ML Components  
**Kind**: struct

A transformer that unwraps optional elements and throws when encountering missing values.

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
struct OptionalUnwrapper<Element>
```

## Topics

### Creating a transformer
- [init()](optionalunwrapper/init.md)
  Creates a transformer that unwraps an optional element or throws if the value is nil.
### Performing the transformation
- [func applied(to: Element?, eventHandler: EventHandler?) throws -> Element](optionalunwrapper/applied(to:eventhandler:).md)
  Unwraps an optional element or throws if the value is `nil`.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)

## See Also

- [struct LinearTransformer](lineartransformer.md)
  A transformer that runs an input through a scale and offset.
- [struct ImputeTransformer](imputetransformer.md)
  A transformer that replaces missing values with a pre-defined value.
- [struct OneHotEncoder](onehotencoder.md)
  An estimator that encodes categorical values to an integer array.
- [struct OrdinalEncoder](ordinalencoder.md)
  An ordinal encoder estimator encodes categorical values to ordinal integer values.
- [struct NumericImputer](numericimputer.md)
  An estimator that replaces missing values in the numeric input.
- [struct Reshaper](reshaper.md)
  A transformer that reshapes a shaped array.
- [struct CategoricalImputer](categoricalimputer.md)
  An estimator that replaces missing values in the categorical input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/optionalunwrapper)*