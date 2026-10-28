# safariDomains

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An array of domain strings for use with Safari-based hotspot authentication.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
final var safariDomains: [String] { get set }
```

## Discussion

The containing app can specify these domains when it intends to use the [`SFSafariViewController`](../../SafariServices/sfsafariviewcontroller.md) class for interacting with the hotspot service provider’s web application during hotspot authentication.

> **Note**: You can specify a maximum of ten domains for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager/safaridomains)*