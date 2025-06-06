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

### Describing the Model Parameter
- [var defaultValue: Any](mlparameterdescription/defaultvalue.md)
  The default value for the parameter.
- [var key: MLParameterKey](mlparameterdescription/key.md)
  The key for this parameter description value.
### Constraining Numeric Values
- [var numericConstraint: MLNumericConstraint?](mlparameterdescription/numericconstraint.md)
  The constraints of this paramter description value, if and only if the value is numerical.
- [class MLNumericConstraint](mlnumericconstraint.md)
  The value limitations of a number.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var isUpdatable: Bool](mlmodeldescription/isupdatable.md)
  A Boolean value that indicates whether you can update the model with additional training.
- [var trainingInputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/traininginputdescriptionsbyname.md)
  A dictionary of the training input feature descriptions, which the model keys by the input’s name.
- [var parameterDescriptionsByKey: [MLParameterKey : MLParameterDescription]](mlmodeldescription/parameterdescriptionsbykey.md)
  A dictionary of the descriptions for the model’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterdescription)*