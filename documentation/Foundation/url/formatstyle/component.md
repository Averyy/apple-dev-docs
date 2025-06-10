# URL.FormatStyle.Component

**Framework**: Foundation  
**Kind**: enum

An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.

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
enum Component
```

#### Overview

You use this type with style-modifying methods like [`displayWhen(_:matches:)`](url/formatstyle/componentdisplayoption/displaywhen(_:matches:).md) in [`URL.FormatStyle.ComponentDisplayOption`](url/formatstyle/componentdisplayoption.md) and [`omitWhen(_:matches:)`](url/formatstyle/hostdisplayoption/omitwhen(_:matches:).md) in [`URL.FormatStyle.HostDisplayOption`](url/formatstyle/hostdisplayoption.md).

## Topics

### URL format style components
- [URL.FormatStyle.Component.scheme](url/formatstyle/component/scheme.md)
  The URL format style scheme component.
- [URL.FormatStyle.Component.host](url/formatstyle/component/host.md)
  The URL format style host component.
- [URL.FormatStyle.Component.port](url/formatstyle/component/port.md)
  The URL format style port component.
- [URL.FormatStyle.Component.user](url/formatstyle/component/user.md)
  The URL format style user component.
- [URL.FormatStyle.Component.password](url/formatstyle/component/password.md)
  The URL format style password component.
- [URL.FormatStyle.Component.path](url/formatstyle/component/path.md)
  The URL format style path component.
- [URL.FormatStyle.Component.query](url/formatstyle/component/query.md)
  The URL format style query component.
- [URL.FormatStyle.Component.fragment](url/formatstyle/component/fragment.md)
  The URL format style fragment component.
### Comparing URL format style components
- [static func != (Self, Self) -> Bool](url/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/component)*