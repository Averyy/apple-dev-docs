# MLParameterDescription

**Framework**: Core ML  
**Kind**: class

A description of a model parameter that includes a default value and a constraint, if applicable.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class MLParameterDescription
```

## Topics

### Describing the model parameter
- [var defaultValue: Any](mlparameterdescription/defaultvalue.md)
  The default value for the parameter.
- [var key: MLParameterKey](mlparameterdescription/key.md)
  The key for this parameter description value.
### Constraining numeric values
- [var numericConstraint: MLNumericConstraint?](mlparameterdescription/numericconstraint.md)
  The constraints of this paramter description value, if and only if the value is numerical.
- [class MLNumericConstraint](mlnumericconstraint.md)
  The value limitations of a number.
### Initializers
- [init?(coder: NSCoder)](mlparameterdescription/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [var isUpdatable: Bool](mlmodeldescription/isupdatable.md)
  A Boolean value that indicates whether you can update the model with additional training.
- [var trainingInputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/traininginputdescriptionsbyname.md)
  A dictionary of the training input feature descriptions, which the model keys by the input’s name.
- [var parameterDescriptionsByKey: [MLParameterKey : MLParameterDescription]](mlmodeldescription/parameterdescriptionsbykey.md)
  A dictionary of the descriptions for the model’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterdescription)*