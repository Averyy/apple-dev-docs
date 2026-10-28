# bundle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A reference to the bundle used for storing the downloaded resources. (read-only)

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use Background Assets instead.

## Declaration

```swift
var bundle: Bundle { get }
```

```objc
@property (strong, readonly) NSBundle * bundle;
```

## Discussion

This value is either the main bundle or the one specified in the call to [`init(tags:bundle:)`](./init%28tags,bundle%29.md). It is valid as soon as the [`NSBundleResourceRequest`](../nsbundleresourcerequest.md) object is created.

## See Also

### Accessing the configuration
- [var tags: Set<String>](./tags.md)
  A set of strings, with each string specifying a tag used to mark on-demand resources managed by the request. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/bundle)*