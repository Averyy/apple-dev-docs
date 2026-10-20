# documentRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Describes the starting and ending locations for the document.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var documentRange: NSTextRange { get }
```

```objc
@property (strong, readonly) NSTextRange * documentRange;
```

#### Discussion

The subclass could use its own implementation of a location object conforming to [`NSTextRange`](../nstextrange.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider/documentrange)*