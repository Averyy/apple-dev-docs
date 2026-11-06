# AppIntent(_:schema:)

**Framework**: App Intents  
**Kind**: macro  
**Role**: Macro

Makes an app intent that conforms to a schema available to Siri as a tool.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@attached(memberAttribute)
@attached(extension, conformances: ToolIntent, AppIntent, AssistantSchemaIntent, ShowInAppSearchResultsIntent, OpenIntent, DeleteIntent, AudioPlaybackIntent, AudioRecordingIntent, LiveActivityIntent, URLRepresentableIntent, names: named(__appSchemaIntent)) macro AppIntent<T>(_ traits: AppIntentTraits, schema: T) where T : AppSchemaIntent
```

## Overview

Use this macro in place of `@AppIntent(schema:)`. It adds everything `@AppIntent(schema:)` adds, plus a [`ToolIntent`](./toolintent.md) conformance:

```swift
@AppIntent(.tool, schema: .journal.createEntry)
struct CreateEntryIntent {
    var title: String?
    var message: AttributedString
    // ...
}
```

Only schemas available exclusively in Shortcuts are supported. Schemas in primary domains, such as `.messages.sendMessage`, are already handled by Siri, and using one here is an error.

## Parameters

- `traits`: The intent’s roles, such as `.tool` or `[.tool]`.
- `schema`: The schema the intent conforms to.

## See Also

### Tool support
- [macro AppIntent(AppIntentTraits)](./appintent%28_%29.md)
  Makes an existing app intent available to Siri as a tool.
- [struct AppIntentTraits](./appintenttraits.md)
  The roles an app intent takes on, passed to `@AppIntent`.
- [struct IntentVisibility](./intentvisibility.md)
  A value that configures how a property is available to system features, such as Siri and Shortcuts, if at all.
- [protocol ToolIntent](./toolintent.md)
  A protocol that identifies an app intent that Siri can call while handling a person’s request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent(_:schema:))*