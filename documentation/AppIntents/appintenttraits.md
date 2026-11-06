# AppIntentTraits

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

The roles an app intent takes on, passed to `@AppIntent`.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct AppIntentTraits
```

## Overview

Pass a single trait, such as `.tool`, or a list, such as `[.tool]`. The macro reads the traits as written, so they have to be listed directly rather than computed.

A set holds each trait at most once. Traits that take a value are compared by trait alone, so two values of the same trait are the same member.

## Topics

### Type Properties
- [static let tool: AppIntentTraits](./appintenttraits/tool.md)
  Siri can call the intent as a tool.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Tool support
- [macro AppIntent(AppIntentTraits)](./appintent%28_%29.md)
  Makes an existing app intent available to Siri as a tool.
- [macro AppIntent<T>(AppIntentTraits, schema: T)](./appintent%28_,schema%29.md)
  Makes an app intent that conforms to a schema available to Siri as a tool.
- [struct IntentVisibility](./intentvisibility.md)
  A value that configures how a property is available to system features, such as Siri and Shortcuts, if at all.
- [protocol ToolIntent](./toolintent.md)
  A protocol that identifies an app intent that Siri can call while handling a person’s request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenttraits)*