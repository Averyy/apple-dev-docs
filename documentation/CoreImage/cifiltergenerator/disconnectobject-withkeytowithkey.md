# disconnectObject(_:withKey:to:withKey:)

**Framework**: Core Image  
**Kind**: method

Removes the connection between two objects in the filter chain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func disconnectObject(_ sourceObject: Any, withKey sourceKey: String, to targetObject: Any, withKey targetKey: String)
```

## Parameters

- `sourceObject`: A [`CIFilter`](cifilter-swift.class.md) object, a  [`CIImage`](ciimage.md) object, or the path (an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object) to an image.
- `sourceKey`: The key that specifies the source object. Pass `nil` if the source object is used directly.
- `targetObject`: The object from which you want to disconnect the source object.
- `targetKey`: The key that specifies the target that the source object is currently connected to.

## See Also

- [func connect(Any, withKey: String?, to: Any, withKey: String)](cifiltergenerator/connect(_:withkey:to:withkey:).md)
  Adds an object to the filter chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/disconnectobject(_:withkey:to:withkey:))*