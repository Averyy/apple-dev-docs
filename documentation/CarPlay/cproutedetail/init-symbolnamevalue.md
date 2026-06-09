# init(symbolName:value:)

**Framework**: CarPlay  
**Kind**: init

Creates custom additional route information with a symbol name and value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(symbolName: String, value: String)
```

#### Return Value

A new @c CPRouteDetail instance with the custom symbol and value

#### Discussion

Use this method to display app-specific route information that doesn’t fit the predefined categories. You provide a custom SF Symbol name and a formatted string value that will be displayed together.

Custom route information provides flexibility for specialized use cases not covered by predefined types. However, the system may not display custom items in as many contexts as predefined information types (toll, fuel, battery, etc.), which receive optimized placement and visual treatment. Use custom information sparingly for truly unique routing characteristics.

> **Note**: Custom route information should be used only when predefined types are insufficient. Consider whether your use case might be addressed by future additions to the framework. If you find yourself creating many custom information types, consider filing enhancement requests for new predefined types that would benefit other developers.

## Parameters

- `symbolName`: An SF Symbol name to display alongside the value. Choose simple, recognizable icons that clearly communicate the information type. Symbol images are rendered as templates and automatically adapt to the current appearance mode (light/dark). Must not be nil.
- `value`: A pre-formatted string to display. The string should be concise and include any necessary units or symbols. The system does not perform additional formatting on custom values, so ensure proper localization and unit conversion in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(symbolname:value:))*