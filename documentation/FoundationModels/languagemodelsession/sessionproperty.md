# LanguageModelSession.SessionProperty

**Framework**: Foundation Models  
**Kind**: struct

A property wrapper that provides access to properties from within profiles,  dynamic instructions, and tools.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@propertyWrapper
struct SessionProperty<Value>
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Overview

Use this to access properties across a language model session, like to access the session history:

```swift
// Get a reference to the session history.
@SessionProperty(\.history)
var history
```

To create a custom session property, use [`SessionPropertyEntry()`](sessionpropertyentry().md) to define a custom key that you access with [`LanguageModelSession.SessionProperty`](languagemodelsession/sessionproperty.md).

## Topics

### Creating a session property
- [init(ReferenceWritableKeyPath<SessionPropertyValues, Value>)](languagemodelsession/sessionproperty/init(_:).md)
  Creates a session property with the specified key path.
### Accessing the property value
- [var wrappedValue: Value](languagemodelsession/sessionproperty/wrappedvalue.md)
  The wrapped value of this property wrapper.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol SessionPropertyKey](sessionpropertykey.md)
  A protocol for defining a custom session property key.
- [class SessionPropertyValues](sessionpropertyvalues.md)
  A container for property values.
- [macro SessionPropertyEntry()](sessionpropertyentry().md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/sessionproperty)*