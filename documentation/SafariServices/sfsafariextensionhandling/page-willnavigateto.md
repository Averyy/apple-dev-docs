# page(_:willNavigateTo:)

**Framework**: Safari Services  
**Kind**: method

A method the system calls when a webpage is about to navigate to a new URL.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func page(_ page: SFSafariPage, willNavigateTo url: URL?)
```

#### Discussion

The `url` parameter is `nil` if the extension does not have permission to access the destination webpage.

## Parameters

- `page`: The webpage from which the user or script initiated the navigation.
- `url`: A URL for the destination webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/page(_:willnavigateto:))*