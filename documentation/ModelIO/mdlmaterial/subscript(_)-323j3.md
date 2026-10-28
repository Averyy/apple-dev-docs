# subscript(_:)

**Framework**: Model I/O  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the material property with the specified name, for use with subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(name: String) -> MDLMaterialProperty? { get }
```

```objc
- (MDLMaterialProperty *) objectForKeyedSubscript:(NSString *) name;
```

## Return Value

The material property with the specified name, or `nil` if the material does not contain a material property with that name.

## Discussion

This method is equivalent to the [`propertyNamed(_:)`](./propertynamed%28_%29.md) method but allows for the use of subscript syntax for reading material properties. To write material properties to the material, use the [`setProperty(_:)`](./setproperty%28_%29.md) method.

## Parameters

- `name`: The [`name`](../mdlmaterialproperty/name.md) value of a material property in the material.

## See Also

### Accessing material properties with subscript syntax
- [subscript(Int) -> MDLMaterialProperty?](./subscript%28_%29-19j2.md)
  Returns the material property at the specified index in the material, for use with subscript syntax.
- [var count: Int](./count.md)
  The number of material properties in the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/subscript(_:)-323j3)*