# connect(_:withKey:to:withKey:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Adds an object to the filter chain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func connect(_ sourceObject: Any, withKey sourceKey: String?, to targetObject: Any, withKey targetKey: String)
```

```objc
- (void) connectObject:(id) sourceObject withKey:(NSString *) sourceKey toObject:(id) targetObject withKey:(NSString *) targetKey;
```

## Parameters

- `sourceObject`: A [`CIFilter`](../cifilter-swift.class.md) object, a  [`CIImage`](../ciimage.md) object, or the path (an [`NSString`](../../Foundation/nsstring.md) or [`NSURL`](../../Foundation/nsurl.md) object) to an image.
- `sourceKey`: The key that specifies the source object. For example, if the source is the output image of a filter, pass the `outputImage` key. Pass `nil` if the source object is used directly.
- `targetObject`: The object to which the source object links.
- `targetKey`: The key that specifies the target for the source. For example, if you are connecting the source to the input image of a [`CIFilter`](../cifilter-swift.class.md) object, you would pass the `inputImage` key.

## See Also

### Connecting and Disconnecting Objects
- [func disconnectObject(Any, withKey: String, to: Any, withKey: String)](./disconnectobject%28_,withkey,to,withkey%29.md)
  Removes the connection between two objects in the filter chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/connect(_:withkey:to:withkey:))*