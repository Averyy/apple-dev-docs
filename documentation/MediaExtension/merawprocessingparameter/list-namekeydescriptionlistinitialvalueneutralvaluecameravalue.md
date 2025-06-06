# list(name:key:description:list:initialValue:neutralValue:cameraValue:)

**Framework**: MediaExtension  
**Kind**: method

**Availability**:
- macOS 15.0+

## Declaration

```swift
class func list(name: String, key: String, description: String, list listElements: [MERAWProcessingParameter.ListElement], initialValue: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.List
```

## See Also

- [class func boolean(name: String, key: String, description: String, initialValue: Bool, neutralValue: Bool?, cameraValue: Bool?) -> MERAWProcessingParameter.Boolean](merawprocessingparameter/boolean(name:key:description:initialvalue:neutralvalue:cameravalue:).md)
- [class func integer(name: String, key: String, description: String, initialValue: Int, maximum: Int, minimum: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.Integer](merawprocessingparameter/integer(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:).md)
- [class func listElement(name: String, description: String, elementID: Int) -> MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement(name:description:elementid:).md)
- [class func subGroup(name: String, description: String, parameters: [MERAWProcessingParameter]) -> MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup(name:description:parameters:).md)
- [class func float(name: String, key: String, description: String, initialValue: Float, maximum: Float, minimum: Float, neutralValue: Float?, cameraValue: Float?) -> MERAWProcessingParameter.FloatingPoint](merawprocessingparameter/float(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/list(name:key:description:list:initialvalue:neutralvalue:cameravalue:))*