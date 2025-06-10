# setDefaultPlaceholder(_:for:with:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func setDefaultPlaceholder(_ placeholder: Any?, for marker: Any?, with binding: NSBindingName)
```

#### Discussion

The `marker` can be `nil` or one of the constants described in [`Selection Markers`](https://developer.apple.com/documentation/AppKit/selection-markers).

## See Also

- [Cocoa Bindings Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)
- [class func defaultPlaceholder(for: Any?, with: NSBindingName) -> Any?](nsobject-swift.class/defaultplaceholder(for:with:).md)
  Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setdefaultplaceholder(_:for:with:))*