# pasteConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The paste configuration associated with the responder object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var pasteConfiguration: UIPasteConfiguration? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIPasteConfiguration * pasteConfiguration;
```

## Discussion

If the responder object doesn’t have a paste configuration, `nil` is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/pasteconfiguration)*