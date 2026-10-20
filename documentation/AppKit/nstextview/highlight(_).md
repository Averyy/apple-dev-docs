# highlight(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An action for toggling `NSTextHighlightStyleAttributeName` in the receiver’s selected range. The sender should be a menu item with a `representedObject` of type (`NSTextHighlightColorScheme`).

**Availability**:
- macOS 15.0+

## Declaration

```swift
@IBAction
func highlight(_ sender: Any?)
```

```objc
- (void) highlight:(id) sender;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/highlight(_:))*