# initWithName:key:description:initialValue:maximum:minimum:neutralValue:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Creates a floating-point parameter object with the initial and neutral values.

**Availability**:
- macOS 15.0+

## Declaration

```objc
- (instancetype) initWithName:(NSString *) name key:(NSString *) key description:(NSString *) description initialValue:(float) initialValue maximum:(float) maximum minimum:(float) minimum neutralValue:(float) neutralValue;
```

## Return Value

An instance of [`MERAWProcessingParameter.FloatingPoint`](../merawprocessingparameter/floatingpoint.md).

## Parameters

- `name`: A localized human-readable name for the parameter, suitable for displaying in application UI.
- `key`: A unique key string identifying this parameter.
- `description`: A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- `initialValue`: The initial value of this parameter as defined in the sequence metadata.
- `maximum`: The maximum value of this parameter.
- `minimum`: The minimum value of this parameter.
- `neutralValue`: The neutral value of this parameter.

## See Also

### Creating a floating-point parameter object
- [- initWithName:key:description:initialValue:maximum:minimum:](./initwithname_key_description_initialvalue_maximum_minimum_.md)
  Creates a floating-point parameter object with the initial value.
- [- initWithName:key:description:initialValue:maximum:minimum:cameraValue:](./initwithname_key_description_initialvalue_maximum_minimum_cameravalue_.md)
  Creates a floating-point parameter object with the initial and camera values.
- [- initWithName:key:description:initialValue:maximum:minimum:neutralValue:cameraValue:](./initwithname_key_description_initialvalue_maximum_minimum_neutralvalue_cameravalue_.md)
  Creates a floating-point parameter object with the initial, neutral, and camera values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingfloatparameter/initwithname:key:description:initialvalue:maximum:minimum:neutralvalue:)*