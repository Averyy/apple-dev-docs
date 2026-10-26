# setObject:forKeyedSubscript:

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(id<MDLComponent>) obj forKeyedSubscript:(Protocol *) key;
```

## See Also

### Object Instancing
- [func atPath(String) -> MDLObject](./atpath%28_%29.md)
  Returns the child object at the specified path.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](./enumeratechildobjects%28of,root,using,stoppointer%29.md)
  Executes the specified block using each object in this object’s child hierarchy.
- [subscript(Protocol) -> (any MDLComponent)?](./subscript%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/setobject:forkeyedsubscript:)*