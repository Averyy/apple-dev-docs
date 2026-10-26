# subscript(_:)

**Framework**: Model I/O  
**Kind**: subscript  
**Role**: Instance Subscript

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

```objc
- (id<MDLComponent>) objectForKeyedSubscript:(Protocol *) key;
```

## See Also

### Object Instancing
- [func atPath(String) -> MDLObject](./atpath%28_%29.md)
  Returns the child object at the specified path.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](./enumeratechildobjects%28of,root,using,stoppointer%29.md)
  Executes the specified block using each object in this object’s child hierarchy.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/subscript(_:))*