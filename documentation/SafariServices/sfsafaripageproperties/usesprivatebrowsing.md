# usesPrivateBrowsing

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the page is using Safari Private Browsing.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var usesPrivateBrowsing: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL usesPrivateBrowsing;
```

## Discussion

[`true`](../../Swift/true.md) if active; otherwise [`false`](../../Swift/false.md).

## See Also

### Getting the Safari Page Properties
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the page is currently active.
- [var title: String?](./title.md)
  The title of the page.
- [var url: URL?](./url.md)
  Indicates the URL of the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/usesprivatebrowsing)*