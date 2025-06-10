# init(description:default:requestValueDialog:inputConnectionBehavior:)

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
convenience init(description: LocalizedStringResource? = nil, default defaultValue: [Value.ValueType?], requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:default:requestvaluedialog:inputconnectionbehavior:)-4khhm)*