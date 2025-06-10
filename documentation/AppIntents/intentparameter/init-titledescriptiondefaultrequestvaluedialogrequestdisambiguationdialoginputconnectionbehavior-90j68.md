# init(title:description:default:requestValueDialog:requestDisambiguationDialog:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(title: LocalizedStringResource, description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, requestValueDialog: IntentDialog? = nil, requestDisambiguationDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `requestDisambiguationDialog`: A prompt that asks a person to choose among possible parameter values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.

## See Also

- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, query: Query)](intentparameter/init(title:description:default:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:query:)-4yyz3.md)
  Creates an app intent parameter with an entity search query.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:resolvers:)-9fsdb.md)
  Creates an app intent parameter that can convert the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:default:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:)-90j68)*