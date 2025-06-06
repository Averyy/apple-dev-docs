# reengagementOpenURLParameter

**Framework**: AdAttributionKit  
**Kind**: property

A string that represents the query parameter that AdAttributionKit appends to the URL to indicate that a reengagement has occurred.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+

## Declaration

```swift
static var reengagementOpenURLParameter: String { get }
```

## Mentions

- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)

#### Discussion

When your advertised app receives a universal link, determine whether it came from an AdAttributionKit reengagement by checking the query parameters for a key containing this string, as the example below shows:

```swift
   func isAdAttributionKitReengagementURL(url: URL) -> Bool {
       guard let components = URLComponents(url: url, resolvingAgainstBaseURL: true),
             let queryItems = components.queryItems else {
           return false
       }
       return queryItems.contains { $0.name == Postback.reengagementOpenURLParameter }
   }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/postback/reengagementopenurlparameter)*