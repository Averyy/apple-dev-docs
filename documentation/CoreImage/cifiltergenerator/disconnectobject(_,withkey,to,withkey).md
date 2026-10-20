# disconnectObject(_:withKey:to:withKey:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Removes the connection between two objects in the filter chain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func disconnectObject(_ sourceObject: Any, withKey sourceKey: String, to targetObject: Any, withKey targetKey: String)
```

```objc
- (void) disconnectObject:(id) sourceObject withKey:(NSString *) sourceKey toObject:(id) targetObject withKey:(NSString *) targetKey;
```

## Parameters

- `sourceObject`: A [`CIFilter`](../cifilter-swift.class.md) object, a  [`CIImage`](../ciimage.md) object, or the path (an [`NSString`](../../Foundation/nsstring.md) or [`NSURL`](../../Foundation/nsurl.md) object) to an image.
- `sourceKey`: The key that specifies the source object. Pass `nil` if the source object is used directly.
- `targetObject`: The object from which you want to disconnect the source object.
- `targetKey`: The key that specifies the target that the source object is currently connected to.

## See Also

### Connecting and Disconnecting Objects
- [func connect(Any, withKey: String?, to: Any, withKey: String)](./connect%28_,withkey,to,withkey%29.md)
  Adds an object to the filter chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/disconnectobject(_:withkey:to:withkey:))*