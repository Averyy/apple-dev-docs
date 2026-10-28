# instancing

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

A flag indicating that function signature uses instancing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var instancing: MTLIntersectionFunctionSignature { get }
```

```c
MTLIntersectionFunctionSignatureInstancing
```

## Discussion

The corresponding MSL function needs to contain the `instancing` tag in its declaration.

## See Also

### Specifying the intersection function signature
- [static var triangleData: MTLIntersectionFunctionSignature](./triangledata.md)
  A flag indicating that function signature uses triangle data.
- [static var worldSpaceData: MTLIntersectionFunctionSignature](./worldspacedata.md)
  A flag indicating that function signature uses world space data.
- [MTLIntersectionFunctionSignatureNone](./mtlintersectionfunctionsignaturenone.md)
  A constant indicating that the function uses the default signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctionsignature/instancing)*