# MLFeatureDescription

**Framework**: Core ML  
**Kind**: class

The name, type, and constraints of an input or output feature.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class MLFeatureDescription
```

#### Overview

In Core ML, a  is a single input or output of a model. A model can have any number of  or . Each feature has a name and a value type, which are defined in the feature’s `MLFeatureDescription`. Model authors use feature descriptions to help developers integrate their model properly. Each `MLFeatureDescription` instance has read-only properties that indicate the feature’s name, its type, and whether it’s optional.

For examples of features, see [`Integrating a Core ML Model into Your App`](integrating-a-core-ml-model-into-your-app.md). Note the three input features named `solarPanels`, `greenhouses`, and `size`, and the output feature is named `price`. All four features are of type `Double`.

An `MLFeatureDescription` may also include constraints, which specify the limitations of the model’s input and output features. For each input feature, the constraints describe what values the model expects from your app. For each output feature, the constraints describe what values your app should expect from the model. You can also write code to inspect these descriptions before using the model in your app.

## Topics

### Inspecting a Feature
- [var name: String](mlfeaturedescription/name.md)
  The name of this feature.
- [var type: MLFeatureType](mlfeaturedescription/type.md)
  The type of this feature.
- [enum MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [var isOptional: Bool](mlfeaturedescription/isoptional.md)
  A Boolean value that indicates whether this feature is optional.
### Checking for Validity
- [func isAllowedValue(MLFeatureValue) -> Bool](mlfeaturedescription/isallowedvalue(_:).md)
  Checks whether the model will accept an input feature value.
### Accessing Feature Constraints
- [var imageConstraint: MLImageConstraint?](mlfeaturedescription/imageconstraint.md)
  The size and format constraints for an image feature.
- [class MLImageConstraint](mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.
- [var dictionaryConstraint: MLDictionaryConstraint?](mlfeaturedescription/dictionaryconstraint.md)
  The constraint for a dictionary feature.
- [class MLDictionaryConstraint](mldictionaryconstraint.md)
  The constraint on the keys for a dictionary feature.
- [var multiArrayConstraint: MLMultiArrayConstraint?](mlfeaturedescription/multiarrayconstraint.md)
  The constraints on a multidimensional array feature.
- [class MLMultiArrayConstraint](mlmultiarrayconstraint.md)
  The shape and data type constraints for a multidimensional array feature.
- [var sequenceConstraint: MLSequenceConstraint?](mlfeaturedescription/sequenceconstraint.md)
  The constraints for a sequence feature.
- [class MLSequenceConstraint](mlsequenceconstraint.md)
  The constraints for a sequence feature.
### Instance Properties
- [var stateConstraint: MLStateConstraint?](mlfeaturedescription/stateconstraint.md)
  The state feature value constraint.

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
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var inputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/inputdescriptionsbyname.md)
  A dictionary of input feature descriptions, which the model keys by the input’s name.
- [var outputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/outputdescriptionsbyname.md)
  A dictionary of output feature descriptions, which the model keys by the output’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturedescription)*