# init(webpageURL:)

**Framework**: Safari Services  
**Kind**: init  
**Role**: Initializer

Creates a universal link object with the URL.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init?(webpageURL url: URL)
```

```objc
- (instancetype) initWithWebpageURL:(NSURL *) url;
```

#### Discussion

This designated initializer creates a [`SFUniversalLink`](../sfuniversallink.md) object.

## Parameters

- `url`: The URL of the web page to associate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfuniversallink/init(webpageurl:))*