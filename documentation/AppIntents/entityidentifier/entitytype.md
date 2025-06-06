# entityType

**Framework**: App Intents  
**Kind**: property

The type of `AppEntity` represented by this identifier

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let entityType: any AppEntity.Type
```

## See Also

- [let identifier: String](entityidentifier/identifier.md)
  Value uniquely identifying the entity instance within its type
- [static let valueMaximumLength: Int](entityidentifier/valuemaximumlength.md)
  Maximum allowed length for the `identifier` value. This is a constraint imposed by the system and thus forces us to truncate the identifier if it exceeds the maximum length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/entitytype)*