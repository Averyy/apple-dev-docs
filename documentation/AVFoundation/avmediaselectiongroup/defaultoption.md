# defaultOption

**Framework**: AVFoundation  
**Kind**: property

The default option in the group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var defaultOption: AVMediaSelectionOption? { get }
```

#### Discussion

The default option is intended for use in the absence of a specific end-user selection or preference. Can be `nil`, indicating that without a specific end-user selection or preference, no option in the group is intended to be selected.

## See Also

- [var options: [AVMediaSelectionOption]](avmediaselectiongroup/options.md)
  A collection of mutually exclusive media selection options
- [func mediaSelectionOption(withPropertyList: Any) -> AVMediaSelectionOption?](avmediaselectiongroup/mediaselectionoption(withpropertylist:).md)
  Returns the media selection options that match the given property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/defaultoption)*