# omitIfHTTPFamily

**Framework**: Foundation  
**Kind**: property

A display option that omits the component if the URL scheme is any flavor of HTTP.

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
static var omitIfHTTPFamily: URL.FormatStyle.ComponentDisplayOption { get }
```

## See Also

- [static var always: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/always.md)
  A display option that always displays the component.
- [static var never: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/never.md)
  A display option that never displays the component.
- [static func displayWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/displaywhen(_:matches:).md)
  Returns a display option that displays the component when a specified component meets the specified requirements.
- [static func omitWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/omitwhen(_:matches:).md)
  Returns a display option that omits the component when a specified component meets the specified requirements.
- [URL.FormatStyle.Component](url/formatstyle/component.md)
  An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/componentdisplayoption/omitifhttpfamily)*