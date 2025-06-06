# isForPrinting

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether you want to print the contents of documents and URLs instead of opening them.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var isForPrinting: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), which causes the app to open documents and URLs. Set the value to [`true`](https://developer.apple.com/documentation/swift/true) if you want the app to print the items instead.

## See Also

- [var requiresUniversalLinks: Bool](nsworkspace/openconfiguration/requiresuniversallinks.md)
  A Boolean value indicating whether you require the URL to have an associated universal link.
- [var requiresUniversalLinks: Bool](nsworkspace/openconfiguration/requiresuniversallinks.md)
  A Boolean value indicating whether you require the URL to have an associated universal link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/isforprinting)*