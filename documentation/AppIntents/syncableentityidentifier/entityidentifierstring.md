# entityIdentifierString

**Framework**: App Intents  
**Kind**: property

Returns the string representation of this identifier’s local ID.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var entityIdentifierString: String { get }
```

#### Return Value

The local ID’s string representation

#### Discussion

This method requires a local ID to be present. Stable-only identifiers (created via the `@_spi(_)` initializer) should not have this method called.

> **Note**: The identifier must have a local ID


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/entityidentifierstring)*