# defaultPlaceholder(for:with:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func defaultPlaceholder(for marker: Any?, with binding: NSBindingName) -> Any?
```

#### Discussion

The `marker` can be `nil` or one of the constants described in [`Selection Markers`](https://developer.apple.com/documentation/AppKit/selection-markers).

## See Also

- [class func setDefaultPlaceholder(Any?, for: Any?, with: NSBindingName)](nsobject-swift.class/setdefaultplaceholder(_:for:with:).md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/defaultplaceholder(for:with:))*