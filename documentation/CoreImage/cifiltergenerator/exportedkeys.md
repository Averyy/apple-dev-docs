# exportedKeys

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

Returns an array of the exported keys.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var exportedKeys: [AnyHashable : Any] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary * exportedKeys;
```

## Return Value

An array of dictionaries that describe the exported key and target object. See [`kCIFilterGeneratorExportedKey`](../kcifiltergeneratorexportedkey.md), [`kCIFilterGeneratorExportedKeyTargetObject`](../kcifiltergeneratorexportedkeytargetobject.md),  and [`kCIFilterGeneratorExportedKey`](../kcifiltergeneratorexportedkey.md) for keys used in the dictionary.

## Discussion

This method returns the keys that you exported using the [`exportKey(_:from:withName:)`](./exportkey%28_,from,withname%29.md) method or that were exported before being written to the file from which you read the filter chain.

## See Also

### Managing Exported Keys
- [func exportKey(String, from: Any, withName: String?)](./exportkey%28_,from,withname%29.md)
  Exports an input or output key of an object in the filter chain.
- [func removeExportedKey(String)](./removeexportedkey%28_%29.md)
  Removes a key that was previously exported.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](./setattributes%28_,forexportedkey%29.md)
  Sets a dictionary of attributes for an exported key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/exportedkeys)*