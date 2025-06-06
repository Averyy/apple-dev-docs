# triangleData

**Framework**: Metal  
**Kind**: property

A flag indicating that function signature uses triangle data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var triangleData: MTLIntersectionFunctionSignature { get }
```

#### Discussion

The corresponding MSL function must contain the `triangle_data` tag in its declaration.

## See Also

- [static var instancing: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/instancing.md)
  A flag indicating that function signature uses instancing.
- [static var worldSpaceData: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/worldspacedata.md)
  A flag indicating that function signature uses world space data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctionsignature/triangledata)*