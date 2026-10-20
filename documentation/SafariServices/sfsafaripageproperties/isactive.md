# isActive

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the page is currently active.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isActive) BOOL active;
```

#### Discussion

[`true`](../../Swift/true.md) if active; otherwise [`false`](../../Swift/false.md).

## See Also

### Getting the Safari Page Properties
- [var title: String?](./title.md)
  The title of the page.
- [var url: URL?](./url.md)
  Indicates the URL of the page.
- [var usesPrivateBrowsing: Bool](./usesprivatebrowsing.md)
  A Boolean value that indicates whether the page is using Safari Private Browsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/isactive)*