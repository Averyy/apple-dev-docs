# shouldResolveExternalEntities

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the parser reports declarations of external entities.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var shouldResolveExternalEntities: Bool { get set }
```

```objc
@property BOOL shouldResolveExternalEntities;
```

## Discussion

[`true`](../../Swift/true.md) if the parser reports declarations of external entities, [`false`](../../Swift/false.md) otherwise. The default value is [`false`](../../Swift/false.md). If you set this property to [`true`](../../Swift/true.md), you may cause other I/O operations, either network-based or disk-based, to load the external DTD.

The parser reports declarations of external entities with the delegate method [`parser(_:foundExternalEntityDeclarationWithName:publicID:systemID:)`](../xmlparserdelegate/parser%28_,foundexternalentitydeclarationwithname,publicid,systemid%29.md).

## See Also

### Managing Parser Behavior
- [var shouldProcessNamespaces: Bool](./shouldprocessnamespaces.md)
  A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [var shouldReportNamespacePrefixes: Bool](./shouldreportnamespaceprefixes.md)
  A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/shouldresolveexternalentities)*