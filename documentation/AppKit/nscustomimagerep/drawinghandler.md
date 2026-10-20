# drawingHandler

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The destination rectangle of the drawing handler block.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var drawingHandler: ((NSRect) -> Bool)? { get }
```

```objc
@property (copy, readonly, nullable) _Bool (^)(struct CGRect) drawingHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomimagerep/drawinghandler)*