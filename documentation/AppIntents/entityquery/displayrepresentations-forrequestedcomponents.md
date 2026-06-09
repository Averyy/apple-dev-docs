# displayRepresentations(for:requestedComponents:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Returns a list of display representation values by identifier based on the requested components.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func displayRepresentations(for identifiers: [Self.Entity.ID], requestedComponents: DisplayRepresentation.Components) async throws -> [Self.Entity.ID : DisplayRepresentation]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquery/displayrepresentations(for:requestedcomponents:))*