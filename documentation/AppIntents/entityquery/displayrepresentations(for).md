# displayRepresentations(for:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns display representations by identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func displayRepresentations(for identifiers: [Self.Entity.ID]) async throws -> [Self.Entity.ID : DisplayRepresentation]
```

#### Discussion

Return full representations; the system materializes only the components it needs (for example, dropping a deferred image when only text is required).

## Default Implementations

### EntityQuery Implementations
- [func displayRepresentations(for: [Self.Entity.ID]) async throws -> [Self.Entity.ID : DisplayRepresentation]](./displayrepresentations%28for%29-258xs.md)
  Returns display representations by identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery/displayrepresentations(for:))*