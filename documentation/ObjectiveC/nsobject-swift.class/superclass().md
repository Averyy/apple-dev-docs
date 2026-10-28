# superclass()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns the class object for the receiver’s superclass.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func superclass() -> AnyClass?
```

```objc
+ (Class) superclass;
```

## Return Value

The class object for the receiver’s superclass.

## See Also

### Related Documentation
- [var superclass: AnyClass?](../nsobjectprotocol/superclass.md)
  Returns the class object for the receiver’s superclass.
- [+ class](./class.md)
  Returns the class object.
### Identifying Classes
- [class func isSubclass(of: AnyClass) -> Bool](./issubclass%28of%29.md)
  Returns a Boolean value that indicates whether the receiving class is a subclass of, or identical to, a given class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/superclass())*