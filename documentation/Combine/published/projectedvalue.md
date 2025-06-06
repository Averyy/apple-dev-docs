# projectedValue

**Framework**: Combine  
**Kind**: property

The property for which this instance exposes a publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var projectedValue: Published<Value>.Publisher { mutating get set }
```

#### Discussion

The [`projectedValue`](published/projectedvalue.md) is the property accessed with the `$` operator.

## See Also

- [Published.Publisher](published/publisher.md)
  A publisher for properties marked with the `@Published` attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/projectedvalue)*