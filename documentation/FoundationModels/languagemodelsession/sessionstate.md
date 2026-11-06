# LanguageModelSession.SessionState

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A property wrapper type that stores session state.

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
@propertyWrapper
struct SessionState<Value>
```

## Overview

Use `@SessionState` to store mutable state that persists across a session’s lifetime.

You can use `@SessionState` as a property wrapper:

```swift
@SessionState var counter: Int = 0
```

## Topics

### Initializers
- [init(wrappedValue: @autoclosure () -> Value)](./sessionstate/init%28wrappedvalue%29.md)
  Creates a session state with a closure providing the initial value.
### Instance Properties
- [var projectedValue: LanguageModelSession.SessionBinding<Value>](./sessionstate/projectedvalue.md)
  A binding to this state for passing to child components.
- [var wrappedValue: Value](./sessionstate/wrappedvalue.md)
  The underlying value.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/sessionstate)*