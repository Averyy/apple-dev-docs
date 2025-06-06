# init(for:summary:optionsCollections:)

**Framework**: App Intents  
**Kind**: init

Creates an object that represents the App Shortcut with the specified parameters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(for keyPath: ParameterKeyPath, summary: AppShortcutParameterPresentationSummary<Intent, Value, Parameter, ParameterKeyPath>, @AppShortcutOptionsCollectionSpecificationBuilder<Value.UnwrappedType> optionsCollections: () -> some AppShortcutOptionsCollectionSpecification<Value.UnwrappedType>)
```

## Parameters

- `summary`: Represents the summary of the parameter used in the presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentation/init(for:summary:optionscollections:))*