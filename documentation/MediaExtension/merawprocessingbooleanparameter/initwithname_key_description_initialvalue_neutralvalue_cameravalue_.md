# initWithName:key:description:initialValue:neutralValue:cameraValue:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Creates a Boolean parameter object with the initial, neutral, and camera values.

**Availability**:
- macOS 15.0+

## Declaration

```objc
- (instancetype) initWithName:(NSString *) name key:(NSString *) key description:(NSString *) description initialValue:(BOOL) initialValue neutralValue:(BOOL) neutralValue cameraValue:(BOOL) cameraValue;
```

#### Return Value

An instance of [`MERAWProcessingParameter.Boolean`](../merawprocessingparameter/boolean.md).

## Parameters

- `name`: A localized human-readable name for the parameter, suitable for displaying in application UI.
- `key`: A unique key string identifying this parameter.
- `description`: A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- `initialValue`: The initial value of this parameter as defined in the sequence metadata.
- `neutralValue`: The neutral value of this parameter.
- `cameraValue`: The camera value for this parameter.

## See Also

### Creating a boolean parameter object
- [- initWithName:key:description:initialValue:](./initwithname_key_description_initialvalue_.md)
  Creates a Boolean parameter object with the initial value.
- [- initWithName:key:description:initialValue:cameraValue:](./initwithname_key_description_initialvalue_cameravalue_.md)
  Creates a Boolean parameter object with the initial and camera values.
- [- initWithName:key:description:initialValue:neutralValue:](./initwithname_key_description_initialvalue_neutralvalue_.md)
  Creates a Boolean parameter object with the initial and neutral values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingbooleanparameter/initwithname:key:description:initialvalue:neutralvalue:cameravalue:)*