# webpageURL

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

The URL specified when initializing the receiver.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var webpageURL: URL { get }
```

```objc
@property (readonly) NSURL * webpageURL;
```

#### Discussion

This property returns the URL passed when initializing the receiver. This property is read-only.

## See Also

### Configuring Universal Links
- [var applicationURL: URL](./applicationurl.md)
  The URL to the app that can open this universal link.
- [var isEnabled: Bool](./isenabled.md)
  A flag that indicates whether the universal link is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfuniversallink/webpageurl)*