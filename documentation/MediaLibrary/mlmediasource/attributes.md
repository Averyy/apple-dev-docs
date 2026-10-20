# attributes

**Framework**: Media Library  
**Kind**: property  
**Role**: Instance Property

A list of attributes describing the media source.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
var attributes: [String : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * attributes;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmediasource/attributes)*