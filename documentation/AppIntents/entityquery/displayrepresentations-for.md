# displayRepresentations(for:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Returns display representations by identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func displayRepresentations(for identifiers: [Self.Entity.ID]) async throws -> [Self.Entity.ID : DisplayRepresentation]
```

#### Discussion

Return full representations; the system materializes only the components it needs (for example, dropping a deferred image when only text is required).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery/displayrepresentations(for:))*