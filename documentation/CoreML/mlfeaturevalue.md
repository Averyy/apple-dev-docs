# MLFeatureValue

**Framework**: Core ML  
**Kind**: class

A generic wrapper around an underlying value and the value’s type.

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
class MLFeatureValue
```

#### Overview

A Core ML  wraps an underlying value and bundles it with that value’s type, which is one of the types that [`MLFeatureType`](mlfeaturetype.md) defines. Apps typically access feature values indirectly by using the methods in the wrapper class Xcode automatically generates for Core ML model files.

If your app accesses an [`MLModel`](mlmodel.md) directly, it must create and consume [`MLFeatureProvider`](mlfeatureprovider.md) instances. For each prediction, Core ML accepts a feature provider for its inputs, and generates a separate feature provider for its outputs. The input feature provider contains one `MLFeatureValue` instance per input, and the output feature provider contains one per output. See [`MLFeatureDescription`](mlfeaturedescription.md) for more information about the model input and output features.

## Topics

### Creating Numeric Feature Values
- [convenience init(int64: Int64)](mlfeaturevalue/init(int64:).md)
  Creates a feature value that contains an integer.
- [convenience init(double: Double)](mlfeaturevalue/init(double:).md)
  Creates a feature value that contains a double.
### Creating String Feature Values
- [convenience init(string: String)](mlfeaturevalue/init(string:).md)
  Creates a feature value that contains a string.
### Creating Multidimensional Feature Values
- [convenience init(multiArray: MLMultiArray)](mlfeaturevalue/init(multiarray:).md)
  Creates a feature value that contains a multidimensional array.
- [convenience init<Scalar>(shapedArray: MLShapedArray<Scalar>)](mlfeaturevalue/init(shapedarray:).md)
  Creates a feature value that contains a shaped array.
### Creating Collection Feature Values
- [convenience init(dictionary: [AnyHashable : NSNumber]) throws](mlfeaturevalue/init(dictionary:).md)
  Creates a feature value that contains a dictionary of numbers.
- [convenience init(sequence: MLSequence)](mlfeaturevalue/init(sequence:).md)
  Creates a feature value that contains a sequence.
### Creating Image Feature Values
- [convenience init(pixelBuffer: CVPixelBuffer)](mlfeaturevalue/init(pixelbuffer:).md)
  Creates a feature value that contains an image from a pixel buffer.
- [convenience init(CGImage: CGImage, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its size and pixel format.
- [convenience init(CGImage: CGImage, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its orientation, size, and pixel format.
- [convenience init(CGImage: CGImage, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and a constraint.
- [convenience init(CGImage: CGImage, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image, an orientation, and a constraint.
- [convenience init(imageAtURL: URL, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s size and pixel format.
- [convenience init(imageAtURL: URL, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s orientation, size, and pixel format.
- [convenience init(imageAtURL: URL, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL and a constraint.
- [convenience init(imageAtURL: URL, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL, an orientation, and a constraint.
- [class MLImageConstraint](mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.
- [MLFeatureValue.ImageOption](mlfeaturevalue/imageoption.md)
  The initializer options you use to crop and scale an image when creating an image feature value.
### Creating Undefined Feature Values
- [convenience init(undefined: MLFeatureType)](mlfeaturevalue/init(undefined:).md)
  Creates a feature value with a type that represents an undefined or missing value.
### Accessing the Feature’s Type
- [var type: MLFeatureType](mlfeaturevalue/type.md)
  The type of the feature value.
### Accessing the Feature’s Value
- [var isUndefined: Bool](mlfeaturevalue/isundefined.md)
  A Boolean value that indicates whether the feature value is undefined or missing.
- [var int64Value: Int64](mlfeaturevalue/int64value.md)
  The underlying integer of the feature value.
- [var doubleValue: Double](mlfeaturevalue/doublevalue.md)
  The underlying double of the feature value.
- [var stringValue: String](mlfeaturevalue/stringvalue.md)
  The underlying string of the feature value.
- [var imageBufferValue: CVPixelBuffer?](mlfeaturevalue/imagebuffervalue.md)
  The underlying image of the feature value as a pixel buffer.
- [func shapedArrayValue<Scalar>(of: Scalar.Type) -> MLShapedArray<Scalar>?](mlfeaturevalue/shapedarrayvalue(of:).md)
  Returns the underlying shaped array of the feature value.
- [var multiArrayValue: MLMultiArray?](mlfeaturevalue/multiarrayvalue.md)
  The underlying multiarray of the feature value.
- [var sequenceValue: MLSequence?](mlfeaturevalue/sequencevalue.md)
  The underlying sequence of the feature value.
- [var dictionaryValue: [AnyHashable : NSNumber]](mlfeaturevalue/dictionaryvalue.md)
  The underlying dictionary of the feature value.
### Comparing Feature Values
- [func isEqual(to: MLFeatureValue) -> Bool](mlfeaturevalue/isequal(to:).md)
  Returns a Boolean value that indicates whether a feature value is equal to another.
### Supporting Types
- [enum MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [struct MLShapedArray](mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.
- [protocol MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.
- [class MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.
- [class MLSequence](mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.
### Initializers
- [convenience init(MLSendableFeatureValue)](mlfeaturevalue/init(_:).md)
  Creates a feature value from a sendable feature value.

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

- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.
- [struct MLSendableFeatureValue](mlsendablefeaturevalue.md)
  A sendable feature value.
- [protocol MLFeatureProvider](mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.
- [class MLDictionaryFeatureProvider](mldictionaryfeatureprovider.md)
  A convenience wrapper for the given dictionary of data.
- [protocol MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.
- [class MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue)*