# url(relativeTo:)

**Framework**: Foundation  
**Kind**: method

Returns a URL object derived from the components object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(relativeTo baseURL: URL?) -> URL?
```

#### Discussion

If the components object has an authority component (user, password, host, or port) and a path component, then the path must either begin with `"/"` or be an empty string. Otherwise, this property contains `nil`.

If the `NSURLComponents` have an authority component (user, password, host, or port) and has a path component, the path component must not start with `"//"`. If it does, this property contains `nil`.

To configure a components object based on an existing URL, call either the [`componentsWithURL:resolvingAgainstBaseURL:`](nsurlcomponents/componentswithurl:resolvingagainstbaseurl:.md) or [`init(url:resolvingAgainstBaseURL:)`](nsurlcomponents/init(url:resolvingagainstbaseurl:).md) method.

## Parameters

- `baseURL`: If non- , this URL is used as the base URL portion of the resulting URL object.

## See Also

- [var string: String?](nsurlcomponents/string.md)
  A URL derived from the components object, in string form.
- [var url: URL?](nsurlcomponents/url.md)
  A URL object derived from the components object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/url(relativeto:))*