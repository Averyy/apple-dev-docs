# init(title:description:default:size:inputConnectionBehavior:query:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an app intent parameter for an array with a specified size per widget family.

**Availability**:
- iOS 17.0+ - Deprecated in 18.0
- iPadOS 17.0+ - Deprecated in 18.0
- Mac Catalyst 17.0+ - Deprecated in 18.0
- macOS 14.0+ - Deprecated in 15.0
- visionOS
- watchOS 10.0+ - Deprecated in 11.0

## Declaration

```swift
convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior = .default, query: Query) where Query : EntityQuery, Value.ValueType == Query.Entity
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, `Value.UnwrappedType` conforms to `Collection`, and `Value.ValueType` conforms to `AppEntity`.

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `size`: The size of the array for a widget family. Use this to limit the amount of values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `query`: A query that Siri and the Shortcuts app can use to retrieve instances of your entity.

## See Also

### Deprecated intiializers
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior)](./init%28title,description,default,size,inputconnectionbehavior%29-7cox5.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./init%28title,description,default,size,inputconnectionbehavior,resolvers%29-1f92a.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, query: Query)](./init%28title,description,default,size,inputconnectionbehavior,query%29-7yfm3.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./init%28title,description,default,size,inputconnectionbehavior,resolvers%29-1f92a.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./init%28title,description,default,size,inputconnectionbehavior,resolvers%29-8o0lz.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior)](./init%28title,description,default,size,inputconnectionbehavior%29-8bfkz.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](./init%28title,description,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,optionsprovider%29.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](./init%28title,description,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,optionsprovider,resolvers%29.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior%29-tfj8.md)
  Creates an app intent parameter.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, query: Query)](./init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,query%29-49n42.md)
  Creates an app intent parameter with an entity search query.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,resolvers%29-1csrx.md)
  Creates an app intent parameter that can convert the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:default:size:inputconnectionbehavior:query:)-1rwev)*