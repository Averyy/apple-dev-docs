# string

**Framework**: AppKit  
**Kind**: property

The characters of the receiver’s text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var string: String { get set }
```

#### Discussion

For performance reasons, this value is the current backing store of the text object. If you want to maintain a snapshot of this as you manipulate the text storage, you should make a copy of the appropriate substring.

## See Also

- [Cocoa Text Architecture Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/string)*