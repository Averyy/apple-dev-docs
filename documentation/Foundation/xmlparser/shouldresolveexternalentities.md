# shouldResolveExternalEntities

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the parser reports declarations of external entities, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. The default value is [`false`](https://developer.apple.com/documentation/swift/false). If you set this property to [`true`](https://developer.apple.com/documentation/swift/true), you may cause other I/O operations, either network-based or disk-based, to load the external DTD.

The parser reports declarations of external entities with the delegate method [`parser(_:foundExternalEntityDeclarationWithName:publicID:systemID:)`](xmlparserdelegate/parser(_:foundexternalentitydeclarationwithname:publicid:systemid:).md).

## See Also

- [var shouldProcessNamespaces: Bool](xmlparser/shouldprocessnamespaces.md)
  A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [var shouldReportNamespacePrefixes: Bool](xmlparser/shouldreportnamespaceprefixes.md)
  A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/shouldresolveexternalentities)*