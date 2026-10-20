# recipients

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the user handles of the desired recipients.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var recipients: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * recipients;
```

#### Discussion

Each object in the array is an `NSString` object that contains the handle of a single recipient. The specific format of these handle varies from service to service. For example, some services use email addresses as handles.

## See Also

### Configuring the Service
- [var menuItemTitle: String](./menuitemtitle.md)
  The title of the service in the Share menu.
- [var subject: String?](./subject.md)
  The subject of the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/recipients)*