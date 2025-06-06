# URL.FormatStyle.ComponentDisplayOption

**Framework**: Foundation  
**Kind**: struct

A type that indicates whether a formatted URL should include a component.

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
struct ComponentDisplayOption
```

## Topics

### Display options
- [static var always: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/always.md)
  A display option that always displays the component.
- [static var never: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/never.md)
  A display option that never displays the component.
- [static var omitIfHTTPFamily: URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/omitifhttpfamily.md)
  A display option that omits the component if the URL scheme is any flavor of HTTP.
- [static func displayWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/displaywhen(_:matches:).md)
  Returns a display option that displays the component when a specified component meets the specified requirements.
- [static func omitWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption/omitwhen(_:matches:).md)
  Returns a display option that omits the component when a specified component meets the specified requirements.
- [URL.FormatStyle.Component](url/formatstyle/component.md)
  An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(scheme: URL.FormatStyle.ComponentDisplayOption, user: URL.FormatStyle.ComponentDisplayOption, password: URL.FormatStyle.ComponentDisplayOption, host: URL.FormatStyle.HostDisplayOption, port: URL.FormatStyle.ComponentDisplayOption, path: URL.FormatStyle.ComponentDisplayOption, query: URL.FormatStyle.ComponentDisplayOption, fragment: URL.FormatStyle.ComponentDisplayOption)](url/formatstyle/init(scheme:user:password:host:port:path:query:fragment:).md)
  Creates a URL format style with the given display options.
- [URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption.md)
  A type that indicates whether a formatted URL should include the host component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/componentdisplayoption)*