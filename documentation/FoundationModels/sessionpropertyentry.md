# SessionPropertyEntry()

**Framework**: Foundation Models  
**Kind**: macro

A macro for defining a custom key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@attached
(accessor) @attached(peer, names: prefixed(__Key_)) macro SessionPropertyEntry()
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Overview

When you need session-scoped properties apply the [`SessionPropertyEntry()`](sessionpropertyentry().md) macro to a stored property in an extension on [`SessionPropertyValues`](sessionpropertyvalues.md):

```swift
extension SessionPropertyValues {
    @SessionPropertyEntry
    var activatedSkills: [String: Bool] = [:]
}
```

Read the shared session state for the custom value by using [`LanguageModelSession.SessionProperty`](languagemodelsession/sessionproperty.md):

```swift
@SessionProperty(\.activatedSkills)
var activatedSkills
```

## See Also

- [LanguageModelSession.SessionProperty](languagemodelsession/sessionproperty.md)
  A property wrapper that provides access to properties from within profiles,  dynamic instructions, and tools.
- [protocol SessionPropertyKey](sessionpropertykey.md)
  A protocol for defining a custom session property key.
- [class SessionPropertyValues](sessionpropertyvalues.md)
  A container for property values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/sessionpropertyentry())*