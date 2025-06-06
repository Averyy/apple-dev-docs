# bundle

**Framework**: Foundation  
**Kind**: property

A reference to the bundle used for storing the downloaded resources. (read-only)

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var bundle: Bundle { get }
```

#### Discussion

This value is either the main bundle or the one specified in the call to [`init(tags:bundle:)`](nsbundleresourcerequest/init(tags:bundle:).md). It is valid as soon as the [`NSBundleResourceRequest`](nsbundleresourcerequest.md) object is created.

## See Also

- [var tags: Set<String>](nsbundleresourcerequest/tags.md)
  A set of strings, with each string specifying a tag used to mark on-demand resources managed by the request. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/bundle)*