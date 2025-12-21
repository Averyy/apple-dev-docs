# requiresUniversalLinks

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether you require the URL to have an associated universal link.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var requiresUniversalLinks: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which tells the app to open any URL you provide. Set the value to [`true`](https://developer.apple.com/documentation/Swift/true) when you want the app to open only valid universal links.

The app must be specifically configured to open universal links, and attempts to open such links fail with an appropriate error if the app isn’t properly configured. Attempts may also fail with an error if the user disabled support for opening links with the specified app.

## See Also

- [var isForPrinting: Bool](nsworkspace/openconfiguration/isforprinting.md)
  A Boolean value indicating whether you want to print the contents of documents and URLs instead of opening them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/requiresuniversallinks)*