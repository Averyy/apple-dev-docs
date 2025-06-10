# NEURLFilter.Verdict

**Framework**: Network Extension  
**Kind**: enum

A verdict returned by a URL filter.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
enum Verdict
```

#### Overview

You receive this type as the result of calling [`verdict(for:)`](neurlfilter/verdict(for:).md) on a [`NEURLFilter`](neurlfilter.md) instance.

## Topics

### Verdicts
- [NEURLFilter.Verdict.allow](neurlfilter/verdict/allow.md)
  A verdict that indicates that accessing the URL is allowed.
- [NEURLFilter.Verdict.deny](neurlfilter/verdict/deny.md)
  A verdict that indicates that accessing the URL is denied.
- [NEURLFilter.Verdict.unknown](neurlfilter/verdict/unknown.md)
  A verdict that indicates URL validation failed.
### Working with raw values
- [init?(rawValue: Int)](neurlfilter/verdict/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func verdict(for: URL) async -> NEURLFilter.Verdict](neurlfilter/verdict(for:).md)
  Determines if accessing the specified URL is allowed or denied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilter/verdict)*