# init(minValue:maxValue:validValues:readOnly:)

**Framework**: Core Media I/O  
**Kind**: init

Creates a property attributes object with the specified configuration.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(minValue: ObjectType?, maxValue: ObjectType?, validValues: [ObjectType]?, readOnly: Bool)
```

#### Discussion

Configure the attributes of a property by optionally specifying:

- A minimum or maximum value to restrict the range of values a property supports.
- An array of valid values to restrict the property to discrete values.

If you don’t specify minimum, maximum, or valid values, the property supports any value.

## Parameters

- `minValue`: An optional minimum value for the property.
- `maxValue`: An optional maximum value for the property.
- `validValues`: An optional array of valid values for the property.
- `readOnly`: A Boolean value that indicates whether the property is read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertyattributes/init(minvalue:maxvalue:validvalues:readonly:))*