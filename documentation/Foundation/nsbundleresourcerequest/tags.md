# tags

**Framework**: Foundation  
**Kind**: property

A set of strings, with each string specifying a tag used to mark on-demand resources managed by the request. (read-only)

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var tags: Set<String> { get }
```

#### Discussion

This value is read-only value and is set when the resource request is initialized. The value of each tag in the set corresponds to an identifier you created during app development.

## See Also

- [var bundle: Bundle](nsbundleresourcerequest/bundle.md)
  A reference to the bundle used for storing the downloaded resources. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/tags)*