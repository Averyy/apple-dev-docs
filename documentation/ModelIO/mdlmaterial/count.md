# count

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The number of material properties in the material.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var count: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger count;
```

## See Also

### Accessing material properties with subscript syntax
- [subscript(String) -> MDLMaterialProperty?](./subscript%28_%29-323j3.md)
  Returns the material property with the specified name, for use with subscript syntax.
- [subscript(Int) -> MDLMaterialProperty?](./subscript%28_%29-19j2.md)
  Returns the material property at the specified index in the material, for use with subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/count)*