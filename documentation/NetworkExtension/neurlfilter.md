# NEURLFilter

**Framework**: Network Extension  
**Kind**: class

A class used to voluntarily validate URLs for apps that don’t use WebKit or the URL session API.

**Availability**:
- iOS 19.0+
- iPadOS 19.0+
- Mac Catalyst 19.0+
- macOS 16.0+

## Declaration

```swift
class NEURLFilter
```

#### Overview

When using networking frameworks other than WebKit or Foundation’s [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), use the `NEURLFilter` API to evaluate URLs before potentially connecting to a restricted or malicious site. Call the class method [`verdict(for:)`](neurlfilter/verdict(for:).md) to check a URL and honor the “allow” or “deny” verdict. Don’t connect to any URL that receives a “deny” verdict.

## Topics

### Evaluating a URL
- [class func verdict(for: URL) async -> NEURLFilter.Verdict](neurlfilter/verdict(for:).md)
  Determines if accessing the specified URL is allowed or denied.
- [NEURLFilter.Verdict](neurlfilter/verdict.md)
  A verdict returned by a URL filter.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEURLFilterManager](neurlfiltermanager.md)
  A class you use to configure and control a URL filter.
- [protocol NEURLFilterControlProvider](neurlfiltercontrolprovider.md)
  A protocol that defines an object that’s responsible for fetching pre-filter data.
- [class NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)
  A class that defines app extension configurations for the URL Filter control provider app extension.
- [Filtering traffic by URL](filtering-traffic-by-url.md)
  Perform fast and robust filtering of full URLs by managing URL filtering configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilter)*