# Publishers.MapKeyPath2.Output

**Framework**: Combine  
**Kind**: typealias  
**Role**: Type Alias

The kind of values published by this publisher.

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
typealias Output = (Output0, Output1)
```

## Discussion

This publisher produces two-element tuples, where each menber’s type matches the type of the corresponding key path’s property.

## See Also

### Declaring supporting types
- [Publishers.MapKeyPath2.Failure](./failure.md)
  The kind of errors this publisher might publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/mapkeypath2/output)*