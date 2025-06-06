# init(viewAnimations:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSViewAnimation` object initialized with the supplied information.

**Availability**:
- macOS ?+

## Declaration

```swift
init(viewAnimations: [[NSViewAnimation.Key : Any]])
```

#### Return Value

The created `NSViewAnimation` object or `nil` if there was a problem initializing the object.

## Parameters

- `viewAnimations`: An array of   objects. Each dictionary specifies a view or window to animate and the effect to apply.   can be  , but you must later set the required array of dictionaries with   if you want to use the capabilities of the   class. See  for a description of valid keys and values for dictionaries in  .

## See Also

- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/init(viewanimations:))*