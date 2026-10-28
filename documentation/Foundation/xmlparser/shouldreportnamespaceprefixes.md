# shouldReportNamespacePrefixes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL shouldReportNamespacePrefixes;
```

## Discussion

[`true`](../../Swift/true.md) if the parser reports the scope of namespace declarations, [`false`](../../Swift/false.md) otherwise. The default value is [`false`](../../Swift/false.md).

The parser reports prefixes with the delegate methods [`parser(_:didStartMappingPrefix:toURI:)`](../xmlparserdelegate/parser%28_,didstartmappingprefix,touri%29.md) and [`parser(_:didEndMappingPrefix:)`](../xmlparserdelegate/parser%28_,didendmappingprefix%29.md).

## See Also

### Managing Parser Behavior
- [var shouldProcessNamespaces: Bool](./shouldprocessnamespaces.md)
  A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [var shouldResolveExternalEntities: Bool](./shouldresolveexternalentities.md)
  A Boolean value that determines whether the parser reports declarations of external entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/shouldreportnamespaceprefixes)*