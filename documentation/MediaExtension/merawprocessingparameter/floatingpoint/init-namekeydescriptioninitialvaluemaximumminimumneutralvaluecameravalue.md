# init(name:key:description:initialValue:maximum:minimum:neutralValue:cameraValue:)

**Framework**: MediaExtension  
**Kind**: init

Creates a floating-point parameter object.

**Availability**:
- macOS 15.0+

## Declaration

```swift
convenience init(name: String, key: String, description: String, initialValue: Float, maximum: Float, minimum: Float, neutralValue: Float? = nil, cameraValue: Float? = nil)
```

## Parameters

- `name`: A localized human-readable name for the parameter, suitable for displaying in application UI.
- `key`: A unique key string identifying this parameter.
- `description`: A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- `initialValue`: The initial value of this parameter as defined in the sequence metadata.
- `maximum`: The maximum value of this parameter.
- `minimum`: The minimum value of this parameter.
- `neutralValue`: The neutral value of this parameter.
- `cameraValue`: The camera value for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/floatingpoint/init(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:))*