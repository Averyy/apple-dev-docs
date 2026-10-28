# NEURLFilter.Verdict

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

A verdict returned by a URL filter.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum Verdict
```

```c
enum NEURLFilterVerdict : NSInteger;
```

## Overview

You receive this type as the result of calling [`verdict(for:)`](./verdict%28for%29.md) on a [`NEURLFilter`](../neurlfilter.md) instance.

## Topics

### Verdicts
- [NEURLFilter.Verdict.allow](./verdict/allow.md)
  A verdict that indicates that accessing the URL is allowed.
- [NEURLFilter.Verdict.deny](./verdict/deny.md)
  A verdict that indicates that accessing the URL is denied.
- [NEURLFilter.Verdict.unknown](./verdict/unknown.md)
  A verdict that indicates URL validation failed.
### Working with raw values
- [init?(rawValue: Int)](./verdict/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Evaluating a URL
- [class func verdict(for: URL) async -> NEURLFilter.Verdict](./verdict%28for%29.md)
  Determines if accessing the specified URL is allowed or denied.
- [+ verdictForURL:completionHandler:](./verdictforurl_completionhandler_.md)
  Determines if accessing the specified URL is allowed or denied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilter/verdict)*