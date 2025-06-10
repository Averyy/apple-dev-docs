# URL.FormatStyle.HostDisplayOption

**Framework**: Foundation  
**Kind**: struct

A type that indicates whether a formatted URL should include the host component.

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
struct HostDisplayOption
```

## Topics

### Display options
- [static var always: URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/always.md)
  A display option that always displays the host component.
- [static var never: URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/never.md)
  A display option that never displays the host component.
- [static var omitIfHTTPFamily: URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/omitifhttpfamily.md)
  A display option that omits the host component if the URL scheme is HTTP or HTTPS.
- [static func displayWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/displaywhen(_:matches:).md)
  Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [static func omitWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/omitwhen(_:matches:).md)
  Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [static func omitSpecificSubdomains(Set<String>, includeMultiLevelSubdomains: Bool) -> URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/omitspecificsubdomains(_:includemultilevelsubdomains:).md)
  Returns a display option that omits the host component if it matches a set of subdomains.
- [static func omitSpecificSubdomains(Set<String>, includeMultiLevelSubdomains: Bool, when: URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/omitspecificsubdomains(_:includemultilevelsubdomains:when:matches:).md)
  Returns a display option that omits the host component if it matches a set of subdomains and a specified component matches a set of requirements.
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(scheme: URL.FormatStyle.ComponentDisplayOption, user: URL.FormatStyle.ComponentDisplayOption, password: URL.FormatStyle.ComponentDisplayOption, host: URL.FormatStyle.HostDisplayOption, port: URL.FormatStyle.ComponentDisplayOption, path: URL.FormatStyle.ComponentDisplayOption, query: URL.FormatStyle.ComponentDisplayOption, fragment: URL.FormatStyle.ComponentDisplayOption)](url/formatstyle/init(scheme:user:password:host:port:path:query:fragment:).md)
  Creates a URL format style with the given display options.
- [URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption.md)
  A type that indicates whether a formatted URL should include a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/hostdisplayoption)*