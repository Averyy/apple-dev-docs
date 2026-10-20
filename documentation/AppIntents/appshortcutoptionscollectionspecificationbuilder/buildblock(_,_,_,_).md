# buildBlock(_:_:_:_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
static func buildBlock<C0, C1, C2, C3>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3) -> some AppShortcutOptionsCollectionSpecification<Value> where C0 : AppShortcutOptionsCollectionProtocol, C1 : AppShortcutOptionsCollectionProtocol, C2 : AppShortcutOptionsCollectionProtocol, C3 : AppShortcutOptionsCollectionProtocol
```

Available when `Value` conforms to `_IntentValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutoptionscollectionspecificationbuilder/buildblock(_:_:_:_:))*