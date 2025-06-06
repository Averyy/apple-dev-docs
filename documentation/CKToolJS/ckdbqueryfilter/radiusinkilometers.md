# radiusInKilometers

**Framework**: CKTool JS  
**Kind**: property

A radius used to determine whether a field that is a location is inside a circular area.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute Double? radiusInKilometers;
```

#### Discussion

This property is only used if the record field indicated by `fieldName` has a value that is a `CKDBLocation` type. When used, the center of the circle is `fieldValue` and the radius is distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbqueryfilter/radiusinkilometers)*