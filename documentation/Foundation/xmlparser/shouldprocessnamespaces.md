# shouldProcessNamespaces

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.

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
var shouldProcessNamespaces: Bool { get set }
```

```objc
@property BOOL shouldProcessNamespaces;
```

#### Discussion

[`true`](../../Swift/true.md) if the parser reports namespace and qualified name, [`false`](../../Swift/false.md) otherwise.

The parser reports element names with the delegate methods [`parser(_:didStartElement:namespaceURI:qualifiedName:attributes:)`](../xmlparserdelegate/parser%28_,didstartelement,namespaceuri,qualifiedname,attributes%29.md) and [`parser(_:didEndElement:namespaceURI:qualifiedName:)`](../xmlparserdelegate/parser%28_,didendelement,namespaceuri,qualifiedname%29.md).

## See Also

### Managing Parser Behavior
- [var shouldReportNamespacePrefixes: Bool](./shouldreportnamespaceprefixes.md)
  A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.
- [var shouldResolveExternalEntities: Bool](./shouldresolveexternalentities.md)
  A Boolean value that determines whether the parser reports declarations of external entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/shouldprocessnamespaces)*