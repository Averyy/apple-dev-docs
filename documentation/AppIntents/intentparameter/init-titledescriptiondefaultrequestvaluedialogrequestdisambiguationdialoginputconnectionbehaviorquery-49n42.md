# init(title:description:default:requestValueDialog:requestDisambiguationDialog:inputConnectionBehavior:query:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with an entity search query.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, requestValueDialog: IntentDialog? = nil, requestDisambiguationDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, query: Query) where Query : EntityQuery, Value.ValueType == Query.Entity
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `requestDisambiguationDialog`: A prompt that asks a person to choose among possible parameter values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `query`: A query that Siri and the Shortcuts app can use to retrieve instances of your entity.

## See Also

- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:size:inputconnectionbehavior:)-7cox5.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:size:inputconnectionbehavior:resolvers:)-1f92a.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior, query: Query)](intentparameter/init(title:description:default:size:inputconnectionbehavior:query:)-1rwev.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, query: Query)](intentparameter/init(title:description:default:size:inputconnectionbehavior:query:)-7yfm3.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:size:inputconnectionbehavior:resolvers:)-1f92a.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:size:inputconnectionbehavior:resolvers:)-8o0lz.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:size:inputconnectionbehavior:)-8bfkz.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:optionsprovider:).md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:optionsprovider:resolvers:).md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:)-tfj8.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:resolvers:)-1csrx.md)
  Creates an app intent parameter that can convert the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:default:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:query:)-49n42)*