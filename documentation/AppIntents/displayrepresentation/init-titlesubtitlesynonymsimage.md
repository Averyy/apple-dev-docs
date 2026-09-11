# init(title:subtitle:synonyms:image:)

**Framework**: App Intents  
**Kind**: init

Creates a display representation whose image is produced lazily by the given closure.

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
init(title: LocalizedStringResource, subtitle: LocalizedStringResource? = nil, synonyms: [LocalizedStringResource] = [], image: @escaping @Sendable () async throws -> DisplayRepresentation.Image?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/displayrepresentation/init(title:subtitle:synonyms:image:))*