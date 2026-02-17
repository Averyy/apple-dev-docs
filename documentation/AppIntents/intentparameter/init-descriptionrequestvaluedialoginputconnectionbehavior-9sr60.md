# init(description:requestValueDialog:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst ?+
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
convenience init(description: LocalizedStringResource? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `description`: Additional details about this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:requestvaluedialog:inputconnectionbehavior:)-9sr60)*