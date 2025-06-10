# URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)

**Framework**: Foundation  
**Kind**: case

A strategy that provides a default value for a component if it’s absent in the source string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case defaultValue(Component)
```

## Parameters

- `Component`: A value to use in the parsed URL if the component is absent in the source string.

## See Also

- [URL.ParseStrategy.ComponentParseStrategy.required](url/parsestrategy/componentparsestrategy/required.md)
  A strategy that requires the presence of the associated component for parsing to succeed.
- [URL.ParseStrategy.ComponentParseStrategy.optional](url/parsestrategy/componentparsestrategy/optional.md)
  A strategy that treats the presence of the associated component as optional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/parsestrategy/componentparsestrategy/defaultvalue(_:))*