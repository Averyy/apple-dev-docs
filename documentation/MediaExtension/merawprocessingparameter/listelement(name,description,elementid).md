# listElement(name:description:elementID:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 15.0+

## Declaration

```swift
class func listElement(name: String, description: String, elementID: Int) -> MERAWProcessingParameter.ListElement
```

## See Also

### Class methods
- [class func boolean(name: String, key: String, description: String, initialValue: Bool, neutralValue: Bool?, cameraValue: Bool?) -> MERAWProcessingParameter.Boolean](./boolean%28name,key,description,initialvalue,neutralvalue,cameravalue%29.md)
- [class func integer(name: String, key: String, description: String, initialValue: Int, maximum: Int, minimum: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.Integer](./integer%28name,key,description,initialvalue,maximum,minimum,neutralvalue,cameravalue%29.md)
- [class func list(name: String, key: String, description: String, list: [MERAWProcessingParameter.ListElement], initialValue: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.List](./list%28name,key,description,list,initialvalue,neutralvalue,cameravalue%29.md)
- [class func subGroup(name: String, description: String, parameters: [MERAWProcessingParameter]) -> MERAWProcessingParameter.SubGroup](./subgroup%28name,description,parameters%29.md)
- [class func float(name: String, key: String, description: String, initialValue: Float, maximum: Float, minimum: Float, neutralValue: Float?, cameraValue: Float?) -> MERAWProcessingParameter.FloatingPoint](./float%28name,key,description,initialvalue,maximum,minimum,neutralvalue,cameravalue%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/listelement(name:description:elementid:))*