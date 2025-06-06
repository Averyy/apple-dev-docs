# displayWhen(_:matches:)

**Framework**: Foundation  
**Kind**: method

Returns a display option that displays the component when a specified component meets the specified requirements.

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
static func displayWhen(_ component: URL.FormatStyle.Component, matches requirements: Set<String>) -> URL.FormatStyle.ComponentDisplayOption
```

#### Return Value

A display option that displays the component when a specified component meets the specified requirements.

## Parameters

- `component`: A component to compare. This may or may not be the component the strategy modifies. For example, a display option for the query might match against known values for the path.
- `requirements`: A set of string values to match against. Matching any member of the set allows the format style to display the component.

## See Also

- [static var always: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/always.md)
  A display option that always displays the component.
- [static var never: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/never.md)
  A display option that never displays the component.
- [static var omitIfHTTPFamily: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/omitifhttpfamily.md)
  A display option that omits the component if the URL scheme is any flavor of HTTP.
- [static func omitWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/omitwhen(_:matches:).md)
  Returns a display option that omits the component when a specified component meets the specified requirements.
- [URL.FormatStyle.Component](url/formatstyle/component.md)
  An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/componentdisplayoption/displaywhen(_:matches:))*