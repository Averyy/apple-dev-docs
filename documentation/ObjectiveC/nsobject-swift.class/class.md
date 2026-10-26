# class

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns the class object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (Class) class;
```

#### Return Value

The class object.

#### Discussion

Refer to a class only by its name when it is the receiver of a message. In all other cases, the class object must be obtained through this or a similar method. For example, here `SomeClass` is passed as an argument to the [`isKind(of:)`](../nsobjectprotocol/iskind%28of%29.md) method (declared in the `NSObject` protocol):

```objc
BOOL test = [self isKindOfClass:[SomeClass class]];
```

## See Also

### Related Documentation
- [func NSStringFromClass(AnyClass) -> String](../../Foundation/nsstringfromclass%28_%29.md)
  Returns the name of a class as a string.
- [- class](../nsobject-c.protocol/class.md)
  Returns the class object for the receiver’s class.
- [func NSClassFromString(String) -> AnyClass?](../../Foundation/nsclassfromstring%28_%29.md)
  Obtains a class by name.
### Identifying Classes
- [class func superclass() -> AnyClass?](./superclass%28%29.md)
  Returns the class object for the receiver’s superclass.
- [class func isSubclass(of: AnyClass) -> Bool](./issubclass%28of%29.md)
  Returns a Boolean value that indicates whether the receiving class is a subclass of, or identical to, a given class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/class)*