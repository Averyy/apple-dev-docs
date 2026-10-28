# initWithName:key:description:list:initialValue:cameraValue:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Creates a list parameter object with the initial and camera values.

**Availability**:
- macOS 15.0+

## Declaration

```objc
- (instancetype) initWithName:(NSString *) name key:(NSString *) key description:(NSString *) description list:(NSArray<MERAWProcessingListElementParameter *> *) listElements initialValue:(NSInteger) initialValue cameraValue:(NSInteger) cameraValue;
```

## Return Value

An instance of [`MERAWProcessingParameter.List`](../merawprocessingparameter/list.md).

## Parameters

- `name`: A localized human-readable name for the parameter, suitable for displaying in application UI.
- `key`: A unique key string identifying this parameter.
- `description`: A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- `listElements`: The ordered array of `MERAWProcessingListElementParameter` objects which make up this list.
- `initialValue`: The initial value of this parameter as defined in the sequence metadata.
- `cameraValue`: The camera value for this parameter.

## See Also

### Creating a list parameter object
- [- initWithName:key:description:list:initialValue:](./initwithname_key_description_list_initialvalue_.md)
  Creates a list parameter object with the initial value.
- [- initWithName:key:description:list:initialValue:neutralValue:](./initwithname_key_description_list_initialvalue_neutralvalue_.md)
  Creates a list parameter object with the initial and neutral values.
- [- initWithName:key:description:list:initialValue:neutralValue:cameraValue:](./initwithname_key_description_list_initialvalue_neutralvalue_cameravalue_.md)
  Creates a list parameter object with the initial, neutral, and camera values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessinglistparameter/initwithname:key:description:list:initialvalue:cameravalue:)*