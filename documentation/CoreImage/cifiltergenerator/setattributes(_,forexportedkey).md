# setAttributes(_:forExportedKey:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Sets a dictionary of attributes for an exported key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setAttributes(_ attributes: [AnyHashable : Any], forExportedKey key: String)
```

```objc
- (void) setAttributes:(NSDictionary *) attributes forExportedKey:(NSString *) key;
```

## Discussion

By default, the exported key inherits the attributes from its original key and target object. You can use this method to change one or more of the existing attributes for the key, such as the default value or maximum value. For more information on attributes, see [`CIFilter`](../cifilter-swift.class.md) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Parameters

- `attributes`: A dictionary that describes the attributes associated with the specified key.
- `key`: The exported key whose attributes you want to set.

## See Also

### Managing Exported Keys
- [var exportedKeys: [AnyHashable : Any]](./exportedkeys.md)
  Returns an array of the exported keys.
- [func exportKey(String, from: Any, withName: String?)](./exportkey%28_,from,withname%29.md)
  Exports an input or output key of an object in the filter chain.
- [func removeExportedKey(String)](./removeexportedkey%28_%29.md)
  Removes a key that was previously exported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/setattributes(_:forexportedkey:))*