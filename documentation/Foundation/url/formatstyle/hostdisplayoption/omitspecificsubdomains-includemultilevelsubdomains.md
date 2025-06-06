# omitSpecificSubdomains(_:includeMultiLevelSubdomains:)

**Framework**: Foundation  
**Kind**: method

Returns a display option that omits the host component if it matches a set of subdomains.

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
static func omitSpecificSubdomains(_ subdomainsToOmit: Set<String> = Set(), includeMultiLevelSubdomains omitMultiLevelSubdomains: Bool = false) -> URL.FormatStyle.HostDisplayOption
```

#### Return Value

A display option that omits the host component if it matches a set of subdomains.

## Parameters

- `subdomainsToOmit`: A set of subdomains to omit, such as  . Matching any member of this set omits the host from the formatted output.
- `omitMultiLevelSubdomains`: A Boolean value to manage display of multi-level subdomains. If  , format style omits additional subdomains if there are more than two in addition to the top-level domain (TLD). For example, when this value is  ,   becomes  , because the TLD is  . By comparison,   has a TLD of  , so it becomes  .

## See Also

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
- [static func omitSpecificSubdomains(Set<String>, includeMultiLevelSubdomains: Bool, when: URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption/omitspecificsubdomains(_:includemultilevelsubdomains:when:matches:).md)
  Returns a display option that omits the host component if it matches a set of subdomains and a specified component matches a set of requirements.
- [URL.FormatStyle.Component](url/formatstyle/component.md)
  An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/hostdisplayoption/omitspecificsubdomains(_:includemultilevelsubdomains:))*