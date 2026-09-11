# init(description:default:size:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter for an array with a specified size.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
convenience init(description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `size`: The size of the array you specify to limit the amount of values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:default:size:inputconnectionbehavior:)-6rm8o)*