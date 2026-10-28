# propertyListFromInputValues()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a property list object that represents the current values for all the input keys of the composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func propertyListFromInputValues() -> Any!
```

```objc
- (id) propertyListFromInputValues;
```

## Return Value

A property list object.

## Discussion

This is a convenience method that allows you to easily save the set of input values on a composition. Typically, you store the set of values in application preferences.

## See Also

### Saving and Restoring Input Values
- [func setInputValuesWithPropertyList(Any!)](./setinputvalueswithpropertylist%28_%29.md)
  Sets the values for the input keys of the composition from a previously saved property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/propertylistfrominputvalues())*