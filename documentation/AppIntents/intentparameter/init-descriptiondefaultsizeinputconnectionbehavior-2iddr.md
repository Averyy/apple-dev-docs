# init(description:default:size:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter for an array with a specified size per widget family.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
convenience init(description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `size`: The size of the array for a widget family. Use this to limit the amount of values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:default:size:inputconnectionbehavior:)-2iddr)*