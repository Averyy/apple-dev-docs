# always

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A display option that always displays the component.

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
static var always: URL.FormatStyle.ComponentDisplayOption { get }
```

## See Also

### Display options
- [static var never: URL.FormatStyle.ComponentDisplayOption](./never.md)
  A display option that never displays the component.
- [static var omitIfHTTPFamily: URL.FormatStyle.ComponentDisplayOption](./omitifhttpfamily.md)
  A display option that omits the component if the URL scheme is any flavor of HTTP.
- [static func displayWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](./displaywhen%28_,matches%29.md)
  Returns a display option that displays the component when a specified component meets the specified requirements.
- [static func omitWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](./omitwhen%28_,matches%29.md)
  Returns a display option that omits the component when a specified component meets the specified requirements.
- [URL.FormatStyle.Component](../component.md)
  An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/componentdisplayoption/always)*