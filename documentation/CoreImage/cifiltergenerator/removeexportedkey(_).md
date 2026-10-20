# removeExportedKey(_:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Removes a key that was previously exported.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func removeExportedKey(_ exportedKeyName: String)
```

```objc
- (void) removeExportedKey:(NSString *) exportedKeyName;
```

## Parameters

- `exportedKeyName`: The name of the key you want to remove.

## See Also

### Managing Exported Keys
- [var exportedKeys: [AnyHashable : Any]](./exportedkeys.md)
  Returns an array of the exported keys.
- [func exportKey(String, from: Any, withName: String?)](./exportkey%28_,from,withname%29.md)
  Exports an input or output key of an object in the filter chain.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](./setattributes%28_,forexportedkey%29.md)
  Sets a dictionary of attributes for an exported key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/removeexportedkey(_:))*