# class()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns `self` (the class object).

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
class func `class`() -> AnyClass
```

```objc
+ (Class) class;
```

## Return Value

`self`. Because this is a class method, it returns the class object

## See Also

### Describing a Proxy Class or Object
- [var description: String](./description.md)
  A string containing the real class name and the id of the receiver as a hexadecimal number.
- [var debugDescription: String](./debugdescription.md)
  A string containing a human-readable description of the receiver suitable for debugging.
### Related Documentation
- [+ class](../../ObjectiveC/nsobject-swift.class/class.md)
  Returns the class object.
- [- class](../../ObjectiveC/nsobject-c.protocol/class.md)
  Returns the class object for the receiver’s class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/class())*