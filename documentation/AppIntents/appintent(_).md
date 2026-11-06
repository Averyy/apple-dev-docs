# AppIntent(_:)

**Framework**: App Intents  
**Kind**: macro  
**Role**: Macro

Makes an existing app intent available to Siri as a tool.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@attached(extension, conformances: ToolIntent)
macro AppIntent(_ traits: AppIntentTraits)
```

## Overview

Apply this macro to a structure or class that conforms to [`AppIntent`](./appintent.md). It adds a [`ToolIntent`](./toolintent.md) conformance, using the availability declared on the type, or the availability of `ToolIntent` when the type declares none.

```swift
@AppIntent(.tool)
struct SearchFlights { ... }
```

## Parameters

- `traits`: The intent’s roles, such as `.tool` or `[.tool]`.

## See Also

### Tool support
- [macro AppIntent<T>(AppIntentTraits, schema: T)](./appintent%28_,schema%29.md)
  Makes an app intent that conforms to a schema available to Siri as a tool.
- [struct AppIntentTraits](./appintenttraits.md)
  The roles an app intent takes on, passed to `@AppIntent`.
- [struct IntentVisibility](./intentvisibility.md)
  A value that configures how a property is available to system features, such as Siri and Shortcuts, if at all.
- [protocol ToolIntent](./toolintent.md)
  A protocol that identifies an app intent that Siri can call while handling a person’s request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent(_:))*