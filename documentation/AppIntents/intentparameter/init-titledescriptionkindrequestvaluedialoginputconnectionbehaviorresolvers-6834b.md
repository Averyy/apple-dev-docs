# init(title:description:kind:requestValueDialog:inputConnectionBehavior:resolvers:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter that can convert the selected value.

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
convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, kind: IntentParameter<Value>.DateKind = .dateTime, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec) where Spec : ResolverSpecification
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `kind`: A value that indicates whether this parameter includes date or time.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `resolvers`: An object that converts a value of another type to this parameter’s type.

## See Also

- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, kind: IntentParameter<Value>.DateKind, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:)-97fq8.md)
  Creates an app intent parameter.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, kind: IntentParameter<Value>.DateKind, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-1adrk.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, kind: IntentParameter<Value>.DateKind, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-3hg6n.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:resolvers:)-6834b)*