# suggestedFocusFilters(for:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

You can implement this method to return a list of suggested focus configurations. This is useful when the suggested focus configurations are different from the configuration when the focus is turned off.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func suggestedFocusFilters(for context: FocusFilterSuggestionContext) async -> [Self]
```

#### Return Value

A list of suggested focus configurations where the first one is the most suggested configuration. Returns an empty array if there is no suggested focus configurations. The system will use the default value per parameters in this case.

## Parameters

- `context`: The focus configuration context which the suggested configurations   could be determined from.

## See Also

- [static var current: Self](setfocusfilterintent/current.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/setfocusfilterintent/suggestedfocusfilters(for:))*