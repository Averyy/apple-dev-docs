# url(scheme:user:password:host:port:path:query:fragment:)

**Framework**: Swift  
**Kind**: method

Creates a regex component that matches a URL substring, capturing it as a Foundation URL.

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
static func url(scheme: URL.ParseStrategy.ComponentParseStrategy<String> = .required, user: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, password: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, host: URL.ParseStrategy.ComponentParseStrategy<String> = .required, port: URL.ParseStrategy.ComponentParseStrategy<Int> = .optional, path: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, query: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, fragment: URL.ParseStrategy.ComponentParseStrategy<String> = .optional) -> Self
```

#### Return Value

A `RegexComponent` that matches a URL.

#### Discussion

All the parameters to this method take a [`URL.ParseStrategy.ComponentParseStrategy`](https://developer.apple.com/documentation/Foundation/URL/ParseStrategy/ComponentParseStrategy) value to configure the matching behavior for one component of the URL. The three possible values are:

- [`URL.ParseStrategy.ComponentParseStrategy.required`](https://developer.apple.com/documentation/Foundation/URL/ParseStrategy/ComponentParseStrategy/required) — The URL component needs to be present for matching to succeed.
- [`URL.ParseStrategy.ComponentParseStrategy.optional`](https://developer.apple.com/documentation/Foundation/URL/ParseStrategy/ComponentParseStrategy/optional) — The URL component doesn’t need to be present for matching to succeed.
- [`URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)`](https://developer.apple.com/documentation/Foundation/URL/ParseStrategy/ComponentParseStrategy/defaultValue(_:)) — If the URL component is absent, the captured URL contains the provided default value for the component.

The following example creates a [`Regex`](regex.md) that matches a URL, when it contains a scheme and a host. It then matches against a source string that contains a date formatted in the `en_US` locale, some whitespace, and a valid URL. The regex defines a default value for the port with [`URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)`](https://developer.apple.com/documentation/Foundation/URL/ParseStrategy/ComponentParseStrategy/defaultValue(_:)), and because the source URL doesn’t include a port, the captured URL adds it.

```swift
let source = "7/31/2022, 5:15:12 AM  https://www.example.com/productList?query=slushie"
let matcher = Regex {
    One(.dateTime(date: .numeric,
                  time: .standard,
                  locale: Locale(identifier: "en_US"),
                  timeZone: TimeZone(identifier: "PST")!))
    OneOrMore(.horizontalWhitespace)
    Capture {
        One(.url(scheme: .required,
                 user: .optional,
                 password: .optional,
                 host: .required,
                 port: .defaultValue(8088),
                 path: .optional,
                 query: .optional,
                 fragment: .optional))
    }
}
guard let match = source.firstMatch(of: matcher) else { return }
let url = match.1 // url = https://www.example.com:8088/productList?query=slushie
```

## Parameters

- `scheme`: A   for matching the URL scheme component.
- `user`: A   for matching the user component.
- `password`: A   for matching the password component.
- `host`: A   for matching the host component.
- `port`: A   for matching the port component.
- `path`: A   for matching the path component.
- `query`: A   for matching the query component.
- `fragment`: A   for matching the fragment component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/url(scheme:user:password:host:port:path:query:fragment:))*