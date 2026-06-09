# init(description:requestValueDialog:inputConnectionBehavior:resolvers:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter that can convert the selected value.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst ?+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
convenience init<Spec>(description: LocalizedStringResource? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec) where Spec : ResolverSpecification
```

## Parameters

- `description`: Additional details about this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `resolvers`: An object that converts a value of another type to this parameter’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:requestvaluedialog:inputconnectionbehavior:resolvers:)-4p921)*