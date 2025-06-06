# subscript(_:)

**Framework**: Model I/O  
**Kind**: subscript

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(key: Protocol) -> (any MDLComponent)? { get set }
```

## See Also

- [func atPath(String) -> MDLObject](mdlobject/atpath(_:).md)
  Returns the child object at the specified path.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](mdlobject/enumeratechildobjects(of:root:using:stoppointer:).md)
  Executes the specified block using each object in this object’s child hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/subscript(_:))*