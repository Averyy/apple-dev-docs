# defaultValue(forKey:)

**Framework**: Core Animation  
**Kind**: method

Specifies the default value associated with the specified key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func defaultValue(forKey key: String) -> Any?
```

#### Return Value

The default value for the named property. Returns `nil` if no default value has been set.

#### Discussion

If you define custom properties for a layer but do not set a value, this method returns a suitable “zero” default value based on the expected value of the `key`. For example, if the value for `key` is a [`CGSize`](https://developer.apple.com/documentation/CoreFoundation/CGSize) struct, the method returns a size struct containing (0.0,0.0) wrapped in an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object. For a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) an empty rectangle is returned. For [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) and [`CATransform3D`](catransform3d.md), the appropriate identity matrix is returned.

##### Special Considerations

If `key` is not a known for property of the class, the result of the method is undefined.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [func shouldArchiveValue(forKey: String) -> Bool](calayer/shouldarchivevalue(forkey:).md)
  Returns a Boolean indicating whether the value of the specified key should be archived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/defaultvalue(forkey:))*