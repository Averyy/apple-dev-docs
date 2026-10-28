# projectedValue

**Framework**: Combine  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The [`projectedValue`](./projectedvalue.md) is the property accessed with the `$` operator.

## See Also

### Publishing the value
- [Published.Publisher](./publisher.md)
  A publisher for properties marked with the `@Published` attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/projectedvalue)*