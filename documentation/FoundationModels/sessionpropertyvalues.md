# SessionPropertyValues

**Framework**: Foundation Models  
**Kind**: class

A container for property values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final class SessionPropertyValues
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Overview

Use session property values across your session. To help manage the context window, access [`history`](sessionpropertyvalues/history.md) to modify the transcript for the session:

```swift
struct CompactingProfile: LanguageModelSession.DynamicProfile {
    @SessionProperty(\.history)
    var history

    var body: some LanguageModelSession.DynamicProfile {
        Profile {
            // Custom instructions and tools that you define.
        }
        .onResponse { _ in
            // Compact the history when the entries exceed a certain limit.
            if history.count > 100 {
                history = Array(history.suffix(50))
            }
        }
    }
}
```

Because updating the transcript history can cause cache invalidations for some models, carefully consider how you modify an existing transcript. For more information, see [`Optimizing key-value caching in language model sessions`](optimizing-key-value-caching-in-language-model-sessions.md).

Use [`SessionPropertyEntry()`](sessionpropertyentry().md) to create custom session properties.

## Topics

### Accessing the session history and instructions
- [var history: ArraySlice<Transcript.Entry>](sessionpropertyvalues/history.md)
  The transcript of the session.
- [var rootDynamicInstructions: any DynamicInstructions](sessionpropertyvalues/rootdynamicinstructions.md)
  The root dynamic instructions.
### Accessing the subscript
- [subscript<K>(K.Type) -> K.Value](sessionpropertyvalues/subscript(_:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelSession.SessionProperty](languagemodelsession/sessionproperty.md)
  A property wrapper that provides access to properties from within profiles,  dynamic instructions, and tools.
- [protocol SessionPropertyKey](sessionpropertykey.md)
  A protocol for defining a custom session property key.
- [macro SessionPropertyEntry()](sessionpropertyentry().md)
  A macro for defining a custom key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/sessionpropertyvalues)*