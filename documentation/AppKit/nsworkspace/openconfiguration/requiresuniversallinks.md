# requiresUniversalLinks

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether you require the URL to have an associated universal link.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var requiresUniversalLinks: Bool { get set }
```

```objc
@property BOOL requiresUniversalLinks;
```

## Discussion

The default value of this property is [`false`](../../../Swift/false.md), which tells the app to open any URL you provide. Set the value to [`true`](../../../Swift/true.md) when you want the app to open only valid universal links.

The app must be specifically configured to open universal links, and attempts to open such links fail with an appropriate error if the app isn’t properly configured. Attempts may also fail with an error if the user disabled support for opening links with the specified app.

## See Also

### Handling URLs
- [var isForPrinting: Bool](./isforprinting.md)
  A Boolean value indicating whether you want to print the contents of documents and URLs instead of opening them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/requiresuniversallinks)*