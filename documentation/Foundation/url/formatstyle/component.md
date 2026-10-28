# URL.FormatStyle.Component

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

You use this type with style-modifying methods like [`displayWhen(_:matches:)`](./componentdisplayoption/displaywhen%28_,matches%29.md) in [`URL.FormatStyle.ComponentDisplayOption`](./componentdisplayoption.md) and [`omitWhen(_:matches:)`](./hostdisplayoption/omitwhen%28_,matches%29.md) in [`URL.FormatStyle.HostDisplayOption`](./hostdisplayoption.md).

## Topics

### URL format style components
- [URL.FormatStyle.Component.scheme](./component/scheme.md)
  The URL format style scheme component.
- [URL.FormatStyle.Component.host](./component/host.md)
  The URL format style host component.
- [URL.FormatStyle.Component.port](./component/port.md)
  The URL format style port component.
- [URL.FormatStyle.Component.user](./component/user.md)
  The URL format style user component.
- [URL.FormatStyle.Component.password](./component/password.md)
  The URL format style password component.
- [URL.FormatStyle.Component.path](./component/path.md)
  The URL format style path component.
- [URL.FormatStyle.Component.query](./component/query.md)
  The URL format style query component.
- [URL.FormatStyle.Component.fragment](./component/fragment.md)
  The URL format style fragment component.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Display options
- [static var always: URL.FormatStyle.ComponentDisplayOption](./componentdisplayoption/always.md)
  A display option that always displays the component.
- [static var never: URL.FormatStyle.ComponentDisplayOption](./componentdisplayoption/never.md)
  A display option that never displays the component.
- [static var omitIfHTTPFamily: URL.FormatStyle.ComponentDisplayOption](./componentdisplayoption/omitifhttpfamily.md)
  A display option that omits the component if the URL scheme is any flavor of HTTP.
- [static func displayWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](./componentdisplayoption/displaywhen%28_,matches%29.md)
  Returns a display option that displays the component when a specified component meets the specified requirements.
- [static func omitWhen(URL.FormatStyle.Component, matches: Set<String>) -> URL.FormatStyle.ComponentDisplayOption](./componentdisplayoption/omitwhen%28_,matches%29.md)
  Returns a display option that omits the component when a specified component meets the specified requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/component)*