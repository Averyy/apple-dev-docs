# AppShortcutOptionsCollection

**Framework**: App Intents  
**Kind**: struct

Represents a collection of options for parameters of an App Shortcut.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct AppShortcutOptionsCollection<Provider> where Provider : DynamicOptionsProvider
```

## Topics

### Initializers
- [init(Provider, title: LocalizedStringResource, systemImageName: String?)](appshortcutoptionscollection/init(_:title:systemimagename:).md)
  Initializes a collection of options for App Shortcuts with the specified parameters.
### Instance Properties
- [let dynamicOptionsProvider: Provider](appshortcutoptionscollection/dynamicoptionsprovider.md)
- [let systemImageName: String?](appshortcutoptionscollection/systemimagename.md)
- [let title: LocalizedStringResource](appshortcutoptionscollection/title.md)

## Relationships

### Conforms To
- [AppShortcutOptionsCollectionProtocol](appshortcutoptionscollectionprotocol.md)

## See Also

- [protocol AppShortcutOptionsCollectionProtocol](appshortcutoptionscollectionprotocol.md)
- [protocol AppShortcutOptionsCollectionSpecification](appshortcutoptionscollectionspecification.md)
- [enum AppShortcutOptionsCollectionSpecificationBuilder](appshortcutoptionscollectionspecificationbuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutoptionscollection)*