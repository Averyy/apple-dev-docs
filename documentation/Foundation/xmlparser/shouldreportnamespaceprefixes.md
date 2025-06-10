# shouldReportNamespacePrefixes

**Framework**: Foundation  
**Kind**: property

A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.

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
var shouldReportNamespacePrefixes: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the parser reports the scope of namespace declarations, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

The parser reports prefixes with the delegate methods [`parser(_:didStartMappingPrefix:toURI:)`](xmlparserdelegate/parser(_:didstartmappingprefix:touri:).md) and [`parser(_:didEndMappingPrefix:)`](xmlparserdelegate/parser(_:didendmappingprefix:).md).

## See Also

- [var shouldProcessNamespaces: Bool](xmlparser/shouldprocessnamespaces.md)
  A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [var shouldResolveExternalEntities: Bool](xmlparser/shouldresolveexternalentities.md)
  A Boolean value that determines whether the parser reports declarations of external entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/shouldreportnamespaceprefixes)*