# init(description:default:supportedContentTypes:size:inputConnectionBehavior:resolvers:)

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
convenience init<Spec>(description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, supportedContentTypes: Array<UTType>? = nil, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior = .default, @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec) where Spec : ResolverSpecification
```

## Parameters

- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `supportedContentTypes`: A list of selectable type identifiers for this parameter.
- `size`: The size of the array you specify to limit the amount of values.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `resolvers`: An object that converts a value of another type to this parameter’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:default:supportedcontenttypes:size:inputconnectionbehavior:resolvers:)-1syql)*