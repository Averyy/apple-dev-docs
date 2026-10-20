# NSMultipleValuesMarker

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

This marker indicates that a key’s value contains multiple values that differ.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```swift
var NSMultipleValuesMarker: AnyObject
```

```c
extern id NSMultipleValuesMarker;
```

#### Discussion

A binding can be configured to always return this marker for multiple items, even if the values are the same.

## See Also

### Deprecated
- [var NSNoSelectionMarker: AnyObject](./nsnoselectionmarker.md)
  This marker indicates that the controller’s selection is currently empty.
- [var NSNotApplicableMarker: AnyObject](./nsnotapplicablemarker.md)
  This marker indicates that an object is not key-value coding compliant for the requested key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmultiplevaluesmarker)*