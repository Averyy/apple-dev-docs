# EmptySnippetIntent

**Framework**: App Intents  
**Kind**: struct

A snippet intent that renders an empty view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct EmptySnippetIntent
```

#### Overview

You don’t create this type directly. AppIntent uses the default value for functions that expect a `SnippetIntent`.

## Topics

### Initializers
- [init()](emptysnippetintent/init.md)
  Creates an app intent.
### Instance Methods
- [func perform() async throws -> some ShowsSnippetView](emptysnippetintent/perform.md)
  Performs the intent after resolving the provided parameters.
### Type Aliases
- [EmptySnippetIntent.PerformResult](emptysnippetintent/performresult.md)
- [EmptySnippetIntent.SummaryContent](emptysnippetintent/summarycontent.md)
  The type of parameter summary representing this intent.
### Type Properties
- [static var isDiscoverable: Bool](emptysnippetintent/isdiscoverable.md)
  A boolean value that determines whether system features such as Shortcuts and Spotlight can discover this app intent.
- [static var title: LocalizedStringResource](emptysnippetintent/title.md)
  A short, localized, human-readable string that describes the app intent using a verb and a noun in title case.
### Default Implementations
- [AppIntent Implementations](emptysnippetintent/appintent-implementations.md)
- [PersistentlyIdentifiable Implementations](emptysnippetintent/persistentlyidentifiable-implementations.md)
- [SnippetIntent Implementations](emptysnippetintent/snippetintent-implementations.md)

## Relationships

### Conforms To
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SnippetIntent](snippetintent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/emptysnippetintent)*