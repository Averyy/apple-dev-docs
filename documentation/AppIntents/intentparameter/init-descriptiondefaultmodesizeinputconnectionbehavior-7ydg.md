# init(description:default:mode:size:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter for an array with a specified size per widget family.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, mode: IntentPerson.ParameterMode = .contact, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `mode`: The user interface that appears when a person chooses a value for this parameter. Default value is  .
- `size`: The size of the array for a widget family. Use this to limit the amount of values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:default:mode:size:inputconnectionbehavior:)-7ydg)*