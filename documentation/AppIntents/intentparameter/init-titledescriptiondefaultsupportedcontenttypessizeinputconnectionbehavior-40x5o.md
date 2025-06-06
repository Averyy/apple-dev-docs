# init(title:description:default:supportedContentTypes:size:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter for an array with a specified size per widget family.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(title: LocalizedStringResource, description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, supportedContentTypes: Array<UTType>? = nil, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `supportedContentTypes`: A list of selectable type identifiers for this parameter.
- `size`: The size of the array for a widget family. Use this to limit the amount of values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:default:supportedcontenttypes:size:inputconnectionbehavior:)-40x5o)*