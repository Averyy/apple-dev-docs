# float(name:key:description:initialValue:maximum:minimum:neutralValue:cameraValue:)

**Framework**: MediaExtension  
**Kind**: method

**Availability**:
- macOS 15.0+

## Declaration

```swift
class func float(name: String, key: String, description: String, initialValue: Float, maximum: Float, minimum: Float, neutralValue: Float?, cameraValue: Float?) -> MERAWProcessingParameter.FloatingPoint
```

## See Also

- [class func boolean(name: String, key: String, description: String, initialValue: Bool, neutralValue: Bool?, cameraValue: Bool?) -> MERAWProcessingParameter.Boolean](merawprocessingparameter/boolean(name:key:description:initialvalue:neutralvalue:cameravalue:).md)
- [class func integer(name: String, key: String, description: String, initialValue: Int, maximum: Int, minimum: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.Integer](merawprocessingparameter/integer(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:).md)
- [class func list(name: String, key: String, description: String, list: [MERAWProcessingParameter.ListElement], initialValue: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.List](merawprocessingparameter/list(name:key:description:list:initialvalue:neutralvalue:cameravalue:).md)
- [class func listElement(name: String, description: String, elementID: Int) -> MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement(name:description:elementid:).md)
- [class func subGroup(name: String, description: String, parameters: [MERAWProcessingParameter]) -> MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup(name:description:parameters:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/float(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:))*