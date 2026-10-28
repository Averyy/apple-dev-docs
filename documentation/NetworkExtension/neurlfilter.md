# NEURLFilter

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A class used to voluntarily validate URLs for apps that don’t use WebKit or the URL session API.

**Availability**:
- iOS 19.0+
- iPadOS 19.0+
- Mac Catalyst 19.0+
- macOS 16.0+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class NEURLFilter
```

```objc
@interface NEURLFilter : NSObject
```

## Overview

When using networking frameworks other than WebKit or Foundation’s [`URLSession`](../Foundation/urlsession.md), use the `NEURLFilter` API to evaluate URLs before potentially connecting to a restricted or malicious site. Call the class method [`verdict(for:)`](./neurlfilter/verdict%28for%29.md) to check a URL and honor the “allow” or “deny” verdict. Don’t connect to any URL that receives a “deny” verdict.

## Topics

### Evaluating a URL
- [class func verdict(for: URL) async -> NEURLFilter.Verdict](./neurlfilter/verdict%28for%29.md)
  Determines if accessing the specified URL is allowed or denied.
- [NEURLFilter.Verdict](./neurlfilter/verdict.md)
  A verdict returned by a URL filter.
- [+ verdictForURL:completionHandler:](./neurlfilter/verdictforurl_completionhandler_.md)
  Determines if accessing the specified URL is allowed or denied.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### URL filters
- [class NEURLFilterManager](./neurlfiltermanager.md)
  A class you use to configure and control a URL filter.
- [protocol NEURLFilterControlProvider](./neurlfiltercontrolprovider.md)
  A protocol that defines an object that’s responsible for fetching pre-filter data.
- [class NEURLFilterControlProviderConfiguration](./neurlfiltercontrolproviderconfiguration.md)
  A class that defines app extension configurations for the URL Filter control provider app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilter)*