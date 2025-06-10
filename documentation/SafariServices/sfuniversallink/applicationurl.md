# applicationURL

**Framework**: Safari Services  
**Kind**: property

The URL to the app that can open this universal link.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var applicationURL: URL { get }
```

#### Discussion

The URL represents a location on the file system. You can retrieve additional information about this app using [`resourceValues(forKeys:)`](https://developer.apple.com/documentation/Foundation/NSURL/resourceValues(forKeys:)).

## See Also

- [var isEnabled: Bool](sfuniversallink/isenabled.md)
  A flag that indicates whether the universal link is enabled.
- [var webpageURL: URL](sfuniversallink/webpageurl.md)
  The URL specified when initializing the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfuniversallink/applicationurl)*