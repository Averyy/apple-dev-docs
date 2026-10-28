# hasCameraValue:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

The optional camera value for this parameter.

**Availability**:
- macOS 15.0+

## Declaration

```objc
- (BOOL) hasCameraValue:(BOOL *) outCameraValue;
```

## Return Value

`YES` if a camera value exists for this parameter; otherwise, `NO`.

## Discussion

This value represents the “as shot” configured camera value for a parameter at the time the media was captured. If the return value is `YES` and `outCameraValue` isn’t `nil`, the value held by `outCameraValue` will be set to the camera value. If the return value is `NO` and `outCameraValue` isn’t `nil`, the value held by `outCameraValue` will be set to `NO`.

## Parameters

- `outCameraValue`: The returned camera value for the parameter.

## See Also

### Inspecting a parameter
- [- hasNeutralValue:](./hasneutralvalue_.md)
  The optional neutral value for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingbooleanparameter/hascameravalue:)*