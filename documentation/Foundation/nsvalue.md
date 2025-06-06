# NSValue

**Framework**: Foundation  
**Kind**: class

A simple container for a single C or Objective-C data item.

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
class NSValue
```

#### Overview

An [`NSValue`](nsvalue.md) object can hold any of the scalar types such as `int`, `float`, and `char`, as well as pointers, structures, and object `id` references. Use this class to work with such data types in collections (such as [`NSArray`](nsarray.md) and [`NSSet`](nsset.md)), [`Key-value coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25), and other APIs that require Objective-C objects. [`NSValue`](nsvalue.md) objects are always immutable.

##### Subclassing Notes

The abstract [`NSValue`](nsvalue.md) class is the public interface of a class cluster consisting mostly of private, concrete classes that create and return a value object appropriate for a given situation. It is possible to subclass [`NSValue`](nsvalue.md), but doing so requires providing storage facilities for the value (which is not inherited by subclasses) and implementing two primitive methods.

###### Methods to Override

Any subclass of [`NSValue`](nsvalue.md)  override the primitive instance methods [`getValue(_:)`](nsvalue/getvalue(_:).md) and [`objCType`](nsvalue/objctype.md). These methods must operate on the storage that you provide for the value.

You might want to implement an initializer for your subclass that is suited to the storage you provide. The [`NSValue`](nsvalue.md) class does not have a designated initializer, so your initializer need only invoke the [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method of `super`. The [`NSValue`](nsvalue.md) class adopts the [`NSCopying`](nscopying.md) and [`NSSecureCoding`](nssecurecoding.md) protocols; if you want instances of your own custom subclass created from copying or coding, override the methods in these protocols.

You may also wish to implement the [`hash`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/hash) method to make your subclass work well in collections.

###### Alternatives to Subclassing

If you need only to use [`NSValue`](nsvalue.md) objects for wrap a custom data types or structures defined by your app, you need not create an [`NSValue`](nsvalue.md) subclass. Instead, create a category that uses existing [`NSValue`](nsvalue.md) methods to store and retrieve data of your custom type. For example, the code below defines a custom Polyhedron structure and creates [`NSValue`](nsvalue.md) convenience methods to store and retrieve it:

```objc
typedef struct {
    int numFaces;
    float radius;
} Polyhedron;
 
@interface NSValue (Polyhedron)
+ (instancetype)valuewithPolyhedron:(Polyhedron)value;
@property (readonly) Polyhedron polyhedronValue;
@end
 
@implementation NSValue (Polyhedron)
+ (instancetype)valuewithPolyhedron:(Polyhedron)value
{
    return [self valueWithBytes:&value objCType:@encode(Polyhedron)];
}
- (Polyhedron) polyhedronValue
{
    Polyhedron value;
    [self getValue:&value];
    return value;
}
@end
```

## Topics

### Working with Raw Values
- [init(bytes: UnsafeRawPointer, objCType: UnsafePointer<CChar>)](nsvalue/init(bytes:objctype:).md)
  Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](nsvalue/init(_:withobjctype:).md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [func getValue(UnsafeMutableRawPointer)](nsvalue/getvalue(_:).md)
  Copies the value into the specified buffer.
- [var objCType: UnsafePointer<CChar>](nsvalue/objctype.md)
  A C string containing the Objective-C type of the data contained in the value object.
### Working with Pointer and Object Values
- [init(pointer: UnsafeRawPointer?)](nsvalue/init(pointer:).md)
  Creates a value object containing the specified pointer.
- [init(nonretainedObject: Any?)](nsvalue/init(nonretainedobject:).md)
  Creates a value object containing the specified object.
- [var pointerValue: UnsafeMutableRawPointer?](nsvalue/pointervalue.md)
  Returns the value as an untyped pointer.
- [var nonretainedObjectValue: Any?](nsvalue/nonretainedobjectvalue.md)
  The value as a non-retained pointer to an object.
### Working with Range Values
- [init(range: NSRange)](nsvalue/init(range:).md)
  Creates a new value object containing the specified Foundation range structure.
- [var rangeValue: NSRange](nsvalue/rangevalue.md)
  The Foundation range structure representation of the value.
### Working with Foundation Geometry Values
- [init(point: NSPoint)](nsvalue/init(point:).md)
  Creates a new value object containing the specified Foundation point structure.
- [init(size: NSSize)](nsvalue/init(size:).md)
  Creates a new value object containing the specified Foundation size structure.
- [init(rect: NSRect)](nsvalue/init(rect:).md)
  Creates a new value object containing the specified Foundation rectangle structure.
- [var pointValue: NSPoint](nsvalue/pointvalue.md)
  The Foundation point structure representation of the value.
- [var sizeValue: NSSize](nsvalue/sizevalue.md)
  The Foundation size structure representation of the value.
- [var rectValue: NSRect](nsvalue/rectvalue.md)
  The Foundation rectangle structure representation of the value.
### Working with CoreGraphics Geometry Values
- [init(CGPoint: CGPoint)](nsvalue/init(cgpoint:).md)
  Creates a new value object containing the specified CoreGraphics point structure.
- [init(CGVector: CGVector)](nsvalue/init(cgvector:).md)
  Creates a new value object containing the specified CoreGraphics vector structure.
- [init(CGSize: CGSize)](nsvalue/init(cgsize:).md)
  Creates a new value object containing the specified CoreGraphics size structure.
- [init(CGRect: CGRect)](nsvalue/init(cgrect:).md)
  Creates a new value object containing the specified CoreGraphics rectangle structure.
- [init(CGAffineTransform: CGAffineTransform)](nsvalue/init(cgaffinetransform:).md)
  Creates a new value object containing the specified CoreGraphics affine transform structure.
- [var cgPointValue: CGPoint](nsvalue/cgpointvalue.md)
  Returns the CoreGraphics point structure representation of the value.
- [var cgVectorValue: CGVector](nsvalue/cgvectorvalue.md)
  Returns the CoreGraphics vector structure representation of the value.
- [var cgSizeValue: CGSize](nsvalue/cgsizevalue.md)
  Returns the CoreGraphics size structure representation of the value.
- [var cgRectValue: CGRect](nsvalue/cgrectvalue.md)
  Returns the CoreGraphics rectangle structure representation of the value.
- [var cgAffineTransformValue: CGAffineTransform](nsvalue/cgaffinetransformvalue.md)
  Returns the CoreGraphics affine transform representation of the value.
### Working with UIKit Geometry Values
- [init(UIEdgeInsets: UIEdgeInsets)](nsvalue/init(uiedgeinsets:).md)
  Creates a new value object containing the specified UIKit edge insets structure.
- [init(UIOffset: UIOffset)](nsvalue/init(uioffset:).md)
  Creates a new value object containing the specified UIKit offset structure.
- [var uiEdgeInsetsValue: UIEdgeInsets](nsvalue/uiedgeinsetsvalue.md)
  Returns the UIKit edge insets structure representation of the value.
- [var uiOffsetValue: UIOffset](nsvalue/uioffsetvalue.md)
  Returns the UIKit offset structure representation of the value.
### Working with CoreAnimation Transform Values
- [init(CATransform3D: CATransform3D)](nsvalue/init(catransform3d:).md)
  Creates a new value object containing the specified CoreAnimation transform structure.
- [var caTransform3DValue: CATransform3D](nsvalue/catransform3dvalue.md)
  The CoreAnimation transform structure representation of the value.
### Working with Media Time Values
- [init(CMTime: CMTime)](nsvalue/init(cmtime:).md)
  Creates a new value object containing the specified CoreMedia time structure.
- [init(CMTimeRange: CMTimeRange)](nsvalue/init(cmtimerange:).md)
  Creates a new value object containing the specified CoreMedia time range structure.
- [init(CMTimeMapping: CMTimeMapping)](nsvalue/init(cmtimemapping:).md)
  Creates a new value object containing the specified CoreMedia time mapping structure.
- [var timeValue: CMTime](nsvalue/timevalue.md)
  The CoreMedia time structure representation of the value.
- [var timeRangeValue: CMTimeRange](nsvalue/timerangevalue.md)
  The CoreMedia time range structure representation of the value.
- [var timeMappingValue: CMTimeMapping](nsvalue/timemappingvalue.md)
  The CoreMedia time mapping structure representation of the value.
### Working with Geographic Coordinate Values
- [init(MKCoordinate: CLLocationCoordinate2D)](nsvalue/init(mkcoordinate:).md)
  Creates a new value object containing the specified CoreLocation geographic coordinate structure.
- [init(MKCoordinateSpan: MKCoordinateSpan)](nsvalue/init(mkcoordinatespan:).md)
  Creates a new value object containing the specified MapKit coordinate span structure.
- [var mkCoordinateValue: CLLocationCoordinate2D](nsvalue/mkcoordinatevalue.md)
  The CoreLocation geographic coordinate structure representation of the value.
- [var mkCoordinateSpanValue: MKCoordinateSpan](nsvalue/mkcoordinatespanvalue.md)
  The MapKit coordinate span structure representation of the value.
### Working with SceneKit Vector and Matrix Values
- [init(SCNVector3: SCNVector3)](nsvalue/init(scnvector3:).md)
  Creates a value object that contains the specified three-element SceneKit vector.
- [init(SCNVector4: SCNVector4)](nsvalue/init(scnvector4:).md)
  Creates a value object that contains the specified four-element SceneKit vector.
- [init(SCNMatrix4: SCNMatrix4)](nsvalue/init(scnmatrix4:).md)
  Creates a value object that contains the specified SceneKit 4 x 4 matrix.
- [var scnVector3Value: SCNVector3](nsvalue/scnvector3value.md)
  The three-element Scene Kit vector representation of the value.
- [var scnVector4Value: SCNVector4](nsvalue/scnvector4value.md)
  The four-element Scene Kit vector representation of the value.
- [var scnMatrix4Value: SCNMatrix4](nsvalue/scnmatrix4value.md)
  The Scene Kit 4 x 4 matrix representation of the value.
### Comparing Value Objects
- [func isEqual(to: NSValue) -> Bool](nsvalue/isequal(to:).md)
  Returns a Boolean value that indicates whether the value object and another value object are equal.
### Initializers
- [init!(CMVideoDimensions: CMVideoDimensions)](nsvalue/init(cmvideodimensions:).md)
- [convenience init(GCPoint2: GCPoint2)](nsvalue/init(gcpoint2:).md)
- [init?(coder: NSCoder)](nsvalue/init(coder:).md)
- [init(directionalEdgeInsets: NSDirectionalEdgeInsets)](nsvalue/init(directionaledgeinsets:).md)
- [init(edgeInsets: NSEdgeInsets)](nsvalue/init(edgeinsets:).md)
### Instance Properties
- [var directionalEdgeInsetsValue: NSDirectionalEdgeInsets](nsvalue/directionaledgeinsetsvalue.md)
- [var edgeInsetsValue: NSEdgeInsets](nsvalue/edgeinsetsvalue.md)
- [var gcPoint2Value: GCPoint2](nsvalue/gcpoint2value.md)
- [var videoDimensionsValue: CMVideoDimensions](nsvalue/videodimensionsvalue.md)
### Instance Methods
- [func getValue(UnsafeMutableRawPointer, size: Int)](nsvalue/getvalue(_:size:).md)
- [func value<StoredType>(of: StoredType.Type) -> StoredType?](nsvalue/value(of:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSNumber](nsnumber.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [class NSNumber](nsnumber.md)
  An object wrapper for primitive scalar numeric values.
- [class ValueTransformer](valuetransformer.md)
  An abstract class used to transform values from one representation to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue)*