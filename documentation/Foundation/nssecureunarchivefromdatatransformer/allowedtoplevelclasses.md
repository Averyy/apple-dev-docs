# allowedTopLevelClasses

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A list of allowed classes the top-level object in an archive must conform to, for encoding and decoding.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class var allowedTopLevelClasses: [AnyClass] { get }
```

```objc
@property (class, copy, readonly) NSArray<Class> * allowedTopLevelClasses;
```

#### Discussion

This property contains the value of [`transformedValueClass()`](../valuetransformer/transformedvalueclass%28%29.md) if that value isn’t `nil`. Otherwise, it holds a list of the top level classes that it decodes, which includes [`NSArray`](../nsarray.md), [`NSDictionary`](../nsdictionary.md), [`NSSet`](../nsset.md), [`NSString`](../nsstring.md), [`NSNumber`](../nsnumber.md), [`NSDate`](../nsdate.md), [`NSData`](../nsdata.md), [`NSURL`](../nsurl.md), [`NSUUID`](../nsuuid.md), and [`NSNull`](../nsnull.md).

Override this property in subclasses to provide an expanded or different set of allowed transformation classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssecureunarchivefromdatatransformer/allowedtoplevelclasses)*