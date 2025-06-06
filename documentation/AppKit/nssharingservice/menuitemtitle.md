# menuItemTitle

**Framework**: AppKit  
**Kind**: property

The title of the service in the Share menu.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var menuItemTitle: String { get set }
```

#### Discussion

By default, this title is the same as the value of the [`title`](nssharingservice/title.md) property. Your app can modify this value.

## See Also

- [var recipients: [String]?](nssharingservice/recipients.md)
  An array containing the user handles of the desired recipients.
- [var subject: String?](nssharingservice/subject.md)
  The subject of the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/menuitemtitle)*