# App entities

**Framework**: App Intents  
**Role**: API Collection

Configure the details for parameter variables that contain custom app entities.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior%29-90j68.md)
  Creates an app intent parameter.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, query: Query)](./intentparameter/init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,query%29-4yyz3.md)
  Creates an app intent parameter with an entity search query.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,resolvers%29-9fsdb.md)
  Creates an app intent parameter that can convert the selected value.
### Deprecated intiializers
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,size,inputconnectionbehavior%29-7cox5.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,size,inputconnectionbehavior,resolvers%29-1f92a.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior, query: Query)](./intentparameter/init%28title,description,default,size,inputconnectionbehavior,query%29-1rwev.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, query: Query)](./intentparameter/init%28title,description,default,size,inputconnectionbehavior,query%29-7yfm3.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,size,inputconnectionbehavior,resolvers%29-1f92a.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,size,inputconnectionbehavior,resolvers%29-8o0lz.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,size,inputconnectionbehavior%29-8bfkz.md)
  Creates an app intent parameter for an array with a specified size.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](./intentparameter/init%28title,description,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,optionsprovider%29.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](./intentparameter/init%28title,description,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,optionsprovider,resolvers%29.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior%29-tfj8.md)
  Creates an app intent parameter.
- [convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, query: Query)](./intentparameter/init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,query%29-49n42.md)
  Creates an app intent parameter with an entity search query.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, requestDisambiguationDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,requestvaluedialog,requestdisambiguationdialog,inputconnectionbehavior,resolvers%29-1csrx.md)
  Creates an app intent parameter that can convert the selected value.

## See Also

### Creating an intent parameter for custom types
- [App enums](./intentparameter-app-enum.md)
  Configure the details for parameter variables that contain custom app enums.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-app-entity)*