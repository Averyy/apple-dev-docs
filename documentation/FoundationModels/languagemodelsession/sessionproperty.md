# LanguageModelSession.SessionProperty

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A property wrapper that provides access to properties from within profiles, dynamic instructions, and tools.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@propertyWrapper
struct SessionProperty<Value>
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](../composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Overview

Use this to access properties across a language model session, like to access the session history:

```swift
// Get a reference to the session history.
@SessionProperty(\.history)
var history
```

To create a custom session property, use [`SessionPropertyEntry()`](../sessionpropertyentry%28%29.md) to define a custom key that you access with [`LanguageModelSession.SessionProperty`](./sessionproperty.md).

## Topics

### Creating a session property
- [init(ReferenceWritableKeyPath<SessionPropertyValues, Value>)](./sessionproperty/init%28_%29.md)
  Creates a session property with the specified key path.
### Accessing the property value
- [var wrappedValue: Value](./sessionproperty/wrappedvalue.md)
  The wrapped value of this property wrapper.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Custom session properties
- [protocol SessionPropertyKey](../sessionpropertykey.md)
  A protocol for defining a custom session property key.
- [class SessionPropertyValues](../sessionpropertyvalues.md)
  A container for property values.
- [macro SessionPropertyEntry()](../sessionpropertyentry%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/sessionproperty)*