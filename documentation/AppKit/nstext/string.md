# string

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The characters of the receiver’s text.

**Availability**:
- macOS

## Declaration

```swift
var string: String { get set }
```

```objc
@property (copy) NSString * string;
```

## Discussion

For performance reasons, this value is the current backing store of the text object. If you want to maintain a snapshot of this as you manipulate the text storage, you should make a copy of the appropriate substring.

## See Also

### Related Documentation
- [Cocoa Text Architecture Guide](https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/string)*