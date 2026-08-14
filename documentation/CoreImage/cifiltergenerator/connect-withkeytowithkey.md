# connect(_:withKey:to:withKey:)

**Framework**: Core Image  
**Kind**: method

Adds an object to the filter chain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func connect(_ sourceObject: Any, withKey sourceKey: String?, to targetObject: Any, withKey targetKey: String)
```

## Parameters

- `sourceObject`: A [`CIFilter`](cifilter-swift.class.md) object, a  [`CIImage`](ciimage.md) object, or the path (an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) or [`NSURL`](https://developer.apple.com/documentation/foundation/nsurl) object) to an image.
- `sourceKey`: The key that specifies the source object. For example, if the source is the output image of a filter, pass the `outputImage` key. Pass `nil` if the source object is used directly.
- `targetObject`: The object to which the source object links.
- `targetKey`: The key that specifies the target for the source. For example, if you are connecting the source to the input image of a [`CIFilter`](cifilter-swift.class.md) object, you would pass the `inputImage` key.

## See Also

- [func disconnectObject(Any, withKey: String, to: Any, withKey: String)](cifiltergenerator/disconnectobject(_:withkey:to:withkey:).md)
  Removes the connection between two objects in the filter chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/connect(_:withkey:to:withkey:))*