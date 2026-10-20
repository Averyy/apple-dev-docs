# connectedTag

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The tag connected to the reader session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
var connectedTag: NFCTag? { get }
```

## See Also

### Connecting to a Tag
- [func connect(to: NFCTag, completionHandler: ((any Error)?) -> Void)](./connect%28to,completionhandler%29.md)
  Connects the reader session to a tag and activates that tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagreadersession/connectedtag-3mlqu)*