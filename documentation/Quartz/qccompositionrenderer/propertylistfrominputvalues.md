# propertyListFromInputValues()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns a property list object that represents the current values for all the input keys of the composition.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func propertyListFromInputValues() -> Any!
```

#### Return Value

A property list object.

#### Discussion

This is a convenience method that allows you to easily save the set of input values on a composition. Typically, you store the set of values in application preferences.

## See Also

- [func setInputValuesWithPropertyList(Any!)](qccompositionrenderer/setinputvalueswithpropertylist(_:).md)
  Sets the values for the input keys of the composition from a previously saved property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/propertylistfrominputvalues())*