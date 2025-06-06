# authorizationViewDidHide(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sent to the delegate to indicate that the view’s visibility has changed.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationViewDidHide(_ view: SFAuthorizationView!)
```

#### Discussion

This delegate method, if present, is called whenever the [`isHidden`](https://developer.apple.com/documentation/AppKit/NSView/isHidden) method is called to show or hide the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewdidhide(_:))*