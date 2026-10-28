# menuItemTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title of the service in the Share menu.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var menuItemTitle: String { get set }
```

```objc
@property (copy) NSString * menuItemTitle;
```

## Discussion

By default, this title is the same as the value of the [`title`](./title.md) property. Your app can modify this value.

## See Also

### Configuring the Service
- [var recipients: [String]?](./recipients.md)
  An array containing the user handles of the desired recipients.
- [var subject: String?](./subject.md)
  The subject of the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/menuitemtitle)*