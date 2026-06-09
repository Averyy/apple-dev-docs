# parseStrategy

**Framework**: Foundation  
**Kind**: property

The strategy used to parse a string into person name components.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var parseStrategy: PersonNameComponents.ParseStrategy { get }
```

## See Also

- [init(String) throws](personnamecomponents/init(_:).md)
  Creates a person name components object from a given string.
- [init<S>(S.ParseInput, strategy: S) throws](personnamecomponents/init(_:strategy:).md)
  Creates a person name components object from a given string by applying the provided parsing strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/parsestrategy)*