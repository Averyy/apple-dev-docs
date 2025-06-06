# path(_:)

**Framework**: Foundation  
**Kind**: method

Modifies a format style to display a URL’s path component in accordance with the provided option.

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
func path(_ strategy: URL.FormatStyle.ComponentDisplayOption = .always) -> URL.FormatStyle
```

#### Return Value

A modified [`URL.FormatStyle`](url/formatstyle.md) that incorporates the specified behavior.

## Parameters

- `strategy`: A component display option that indicates when, if ever, to display the path component.

## See Also

- [func scheme(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/scheme(_:).md)
  Modifies a format style to display a URL’s scheme component in accordance with the provided option.
- [func user(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/user(_:).md)
  Modifies a format style to display a URL’s user component in accordance with the provided option.
- [func password(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/password(_:).md)
  Modifies a format style to display a URL’s password component in accordance with the provided option.
- [func host(URL.FormatStyle.HostDisplayOption) -> URL.FormatStyle](url/formatstyle/host(_:).md)
  Modifies a format style to display a URL’s host component in accordance with the provided option.
- [URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption.md)
  A type that indicates whether a formatted URL should include the host component.
- [func port(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/port(_:).md)
  Modifies a format style to display a URL’s port component in accordance with the provided option.
- [func query(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/query(_:).md)
  Modifies a format style to display a URL’s query component in accordance with the provided option.
- [func fragment(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/fragment(_:).md)
  Modifies a format style to display a URL’s fragment component in accordance with the provided option.
- [URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption.md)
  A type that indicates whether a formatted URL should include a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle/path(_:))*