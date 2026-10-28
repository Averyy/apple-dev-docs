# omitSpecificSubdomains(_:includeMultiLevelSubdomains:when:matches:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a display option that omits the host component if it matches a set of subdomains and a specified component matches a set of requirements.

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
static func omitSpecificSubdomains(_ subdomainsToOmit: Set<String> = Set(), includeMultiLevelSubdomains omitMultiLevelSubdomains: Bool = false, when component: URL.FormatStyle.Component, matches requirements: Set<String>) -> URL.FormatStyle.HostDisplayOption
```

## Return Value

A display option that omits the host component if it matches a set of subdomains and a specified component meets the specified requirements.

## Parameters

- `subdomainsToOmit`: A set of subdomains to omit, such as `[”www”, “mobile”, “m”]`. Matching any member of this set omits the host from the formatted output.
- `omitMultiLevelSubdomains`: A Boolean value to manage display of multi-level subdomains. If `true`, format style omits additional subdomains if there are more than two in addition to the top-level domain (TLD). For example, when this value is `true`, `api.code.developer.example.com` becomes `developer.example.com`, because the TLD is `“com”`. By comparison, `api.code.developer.example.com.cn` has a TLD of `“com.cn”`, so it becomes `developer.example.com.cn`.
- `component`: A component to compare. This may or may not be the host component itself.
- `requirements`: A set of string values to match against. Matching any member of the set informs the format style to omit the component.

## See Also

### Display options
- [static var always: URL.FormatStyle.HostDisplayOption](./always.md)
  A display option that always displays the host component.
- [static var never: URL.FormatStyle.HostDisplayOption](./never.md)
  A display option that never displays the host component.
- [static var omitIfHTTPFamily: URL.FormatStyle.HostDisplayOption](./omitifhttpfamily.md)
  A display option that omits the host component if the URL scheme is HTTP or HTTPS.
- [static func displayWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.HostDisplayOption](./displaywhen%28_,matches%29.md)
  Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [static func omitWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.HostDisplayOption](./omitwhen%28_,matches%29.md)
  Returns a display option that displays the host component when a specified component matches against a set of requirement values.
- [static func omitSpecificSubdomains(Set<String>, includeMultiLevelSubdomains: Bool) -> URL.FormatStyle.HostDisplayOption](./omitspecificsubdomains%28_,includemultilevelsubdomains%29.md)
  Returns a display option that omits the host component if it matches a set of subdomains.
- [URL.FormatStyle.Component](../component.md)
  An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/hostdisplayoption/omitspecificsubdomains(_:includemultilevelsubdomains:when:matches:))*