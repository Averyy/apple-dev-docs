# ValueTransformer

**Framework**: Foundation  
**Kind**: class

An abstract class used to transform values from one representation to another.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class ValueTransformer
```

#### Overview

You create a value transformer by subclassing [`ValueTransformer`](valuetransformer.md) and overriding the necessary methods to provide the required custom transformation. You then register the value transformer using the [`setValueTransformer(_:forName:)`](valuetransformer/setvaluetransformer(_:forname:).md) method, so that other parts of your app can access it by name with [`init(forName:)`](valuetransformer/init(forname:).md).

Use the [`transformedValue(_:)`](valuetransformer/transformedvalue(_:).md) method to transform a value from one representation into another. If a value transformer designates that its transformation is reversible by returning [`true`](https://developer.apple.com/documentation/Swift/true) for [`allowsReverseTransformation()`](valuetransformer/allowsreversetransformation().md), you can also use the [`reverseTransformedValue(_:)`](valuetransformer/reversetransformedvalue(_:).md) to perform the transformation in reverse. For example, reversing the characters in a string is a reversible operation, whereas changing the characters in a string to be uppercase is a nonreversible operation.

A value transformer can take inputs of one type and return a value of a different type. For example,  a value transformer could take an [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) or [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object and return an [`NSData`](nsdata.md) object containing the PNG representation of that image.

##### Example Usage

The following example defines a new value transformer that takes an object and returns a string based on the object’s class type. This transformer isn’t reversible because it doesn’t make sense to transform a class name into an object.

## Topics

### Using the Name-Based Registry
- [class func setValueTransformer(ValueTransformer?, forName: NSValueTransformerName)](valuetransformer/setvaluetransformer(_:forname:).md)
  Registers the provided value transformer with a given identifier.
- [init?(forName: NSValueTransformerName)](valuetransformer/init(forname:).md)
  Returns the value transformer identified by a given identifier.
- [class func valueTransformerNames() -> [NSValueTransformerName]](valuetransformer/valuetransformernames.md)
  Returns an array of all the registered value transformers.
- [struct NSValueTransformerName](nsvaluetransformername.md)
  Named value transformers defined by `NSValueTransformer`.
### Getting Information About a Transformer
- [class func allowsReverseTransformation() -> Bool](valuetransformer/allowsreversetransformation.md)
  Returns a Boolean value that indicates whether the receiver can reverse a transformation.
- [class func transformedValueClass() -> AnyClass](valuetransformer/transformedvalueclass.md)
  Returns the class of the value returned by the receiver for a forward transformation.
### Transforming Values
- [func transformedValue(Any?) -> Any?](valuetransformer/transformedvalue(_:).md)
  Returns the result of transforming a given value.
- [func reverseTransformedValue(Any?) -> Any?](valuetransformer/reversetransformedvalue(_:).md)
  Returns the result of the reverse transformation of a given value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSNumber](nsnumber.md)
  An object wrapper for primitive scalar numeric values.
- [class NSValue](nsvalue.md)
  A simple container for a single C or Objective-C data item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/valuetransformer)*