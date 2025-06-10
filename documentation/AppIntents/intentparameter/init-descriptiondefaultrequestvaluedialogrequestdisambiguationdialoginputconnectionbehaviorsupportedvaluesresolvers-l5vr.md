# init(description:default:requestValueDialog:requestDisambiguationDialog:inputConnectionBehavior:supportedValues:resolvers:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter that can convert the selected value.

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
convenience init<Spec>(description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, requestValueDialog: IntentDialog? = nil, requestDisambiguationDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, supportedValues: [Value.ValueType] = Array(Value.ValueType.allCases), @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec) where Spec : ResolverSpecification
```

## Parameters

- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `requestDisambiguationDialog`: A prompt that asks a person to choose among possible parameter values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `supportedValues`: A list of selectable options for this parameter.
- `resolvers`: An object that converts a value of another type to this parameter’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:default:requestvaluedialog:requestdisambiguationdialog:inputconnectionbehavior:supportedvalues:resolvers:)-l5vr)*