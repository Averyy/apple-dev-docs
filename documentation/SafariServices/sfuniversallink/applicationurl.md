# applicationURL

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

The URL to the app that can open this universal link.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var applicationURL: URL { get }
```

```objc
@property (readonly) NSURL * applicationURL;
```

#### Discussion

The URL represents a location on the file system. You can retrieve additional information about this app using [`resourceValues(forKeys:)`](../../Foundation/nsurl/resourcevalues%28forkeys%29.md).

## See Also

### Configuring Universal Links
- [var isEnabled: Bool](./isenabled.md)
  A flag that indicates whether the universal link is enabled.
- [var webpageURL: URL](./webpageurl.md)
  The URL specified when initializing the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfuniversallink/applicationurl)*