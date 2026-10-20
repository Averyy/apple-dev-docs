# setInputValuesWithPropertyList(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the values for the input keys of the composition from a previously saved property list.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setInputValuesWithPropertyList(_ plist: Any!)
```

```objc
- (void) setInputValuesWithPropertyList:(id) plist;
```

#### Discussion

This is a convenience method that allows you to restore the set of input values that you obtained previously by calling the method [`propertyListFromInputValues()`](./propertylistfrominputvalues%28%29.md). If the property list object does not define a value for an input key, or if the value is not of the proper type, Quartz Composer does not set a value for the corresponding input port.

## See Also

### Saving and Restoring Input Values
- [func propertyListFromInputValues() -> Any!](./propertylistfrominputvalues%28%29.md)
  Returns a property list object that represents the current values for all the input keys of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/setinputvalueswithpropertylist(_:))*