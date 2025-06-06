# setInputValuesWithPropertyList(_:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Sets the values for the input keys of the composition from a previously saved property list.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setInputValuesWithPropertyList(_ plist: Any!)
```

#### Discussion

This is a convenience method that allows you to restore the set of input values that you obtained previously by calling the method [`propertyListFromInputValues()`](qccompositionrenderer/propertylistfrominputvalues().md). If the property list object does not define a value for an input key, or if the value is not of the proper type, Quartz Composer does not set a value for the corresponding input port.

## See Also

- [func propertyListFromInputValues() -> Any!](qccompositionrenderer/propertylistfrominputvalues.md)
  Returns a property list object that represents the current values for all the input keys of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/setinputvalueswithpropertylist(_:))*