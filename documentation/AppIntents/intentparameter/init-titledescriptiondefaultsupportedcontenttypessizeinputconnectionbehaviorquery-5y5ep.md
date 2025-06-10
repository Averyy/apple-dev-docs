# init(title:description:default:supportedContentTypes:size:inputConnectionBehavior:query:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter for an array with a specified size.

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
convenience init<Query>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, supportedContentTypes: Array<UTType>? = nil, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior = .default, query: Query) where Query : EntityQuery, Value.ValueType == Query.Entity
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `supportedContentTypes`: A list of selectable type identifiers for this parameter.
- `size`: The size of the array you specify to limit the amount of values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `query`: A query that Siri and the Shortcuts app can use to retrieve instances of your entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:default:supportedcontenttypes:size:inputconnectionbehavior:query:)-5y5ep)*