# init(description:defaultValue:defaultUnit:defaultUnitAdjustForLocale:supportsNegativeNumbers:requestValueDialog:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with a default unit for the measurement.

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
convenience init(description: LocalizedStringResource? = nil, defaultValue: Double? = nil, defaultUnit: IntentParameter<Value>.Temperature? = nil, defaultUnitAdjustForLocale: Bool = false, supportsNegativeNumbers: Bool = true, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `defaultUnit`: The default unit that should be selected when this parameter is initially created.
- `defaultUnitAdjustForLocale`: Whether or not the default unit should adjust to match someone’s locale. Default value is  .
- `supportsNegativeNumbers`: Whether or not this parameter supports negative number inputs. Default value is  .
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:defaultvalue:defaultunit:defaultunitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:)-7v8en)*