# hasNeutralValue:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

The optional neutral value for this parameter.

**Availability**:
- macOS 15.0+

## Declaration

```objc
- (BOOL) hasNeutralValue:(NSInteger *) outNeutralValue;
```

## Return Value

`YES` if a neutral value exists for this parameter; otherwise, `NO`.

## Discussion

If the return value is `YES` and `outNeutralValue` isn’t `nil`, the value held by `outNeutralValue` will be set to the neutral value. If the return value is `NO` and `outNeutralValue` isn’t `nil`, the value held by `outNeutralValue` is 0.

## Parameters

- `outNeutralValue`: The returned neutral value for the parameter.

## See Also

### Inspecting a parameter
- [- hasCameraValue:](./hascameravalue_.md)
  The optional camera value for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessinglistparameter/hasneutralvalue:)*