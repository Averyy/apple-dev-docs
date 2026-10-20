# subscript(_:)

**Framework**: Model I/O  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the material property at the specified index in the material, for use with subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(idx: Int) -> MDLMaterialProperty? { get }
```

```objc
- (MDLMaterialProperty *) objectAtIndexedSubscript:(NSUInteger) idx;
```

#### Return Value

The material property at the specified index.

#### Discussion

The ordering of material properties in a material is arbitrary, but you can use this method (together with the count property) to iterate through the material’s complete list of material properties. You can also iterate through material properties using [Fast Enumeration](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Enumeration.html#//apple_ref/doc/uid/TP40008195-CH17-SW3).

## Parameters

- `idx`: An index in the material’s list of material properties; must be less than the value of [`count`](./count.md).

## See Also

### Accessing material properties with subscript syntax
- [subscript(String) -> MDLMaterialProperty?](./subscript%28_%29-323j3.md)
  Returns the material property with the specified name, for use with subscript syntax.
- [var count: Int](./count.md)
  The number of material properties in the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/subscript(_:)-19j2)*