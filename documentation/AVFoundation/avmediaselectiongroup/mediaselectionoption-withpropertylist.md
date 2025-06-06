# mediaSelectionOption(withPropertyList:)

**Framework**: AVFoundation  
**Kind**: method

Returns the media selection options that match the given property list.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func mediaSelectionOption(withPropertyList plist: Any) -> AVMediaSelectionOption?
```

#### Return Value

An [`AVMediaSelectionOption`](avmediaselectionoption.md) object containing the properites passed by `plist`. Returns `nil` when no match is found.

## Parameters

- `plist`: A property list previously obtained from an option in the group using   ( ).

## See Also

- [var options: [AVMediaSelectionOption]](avmediaselectiongroup/options.md)
  A collection of mutually exclusive media selection options
- [var defaultOption: AVMediaSelectionOption?](avmediaselectiongroup/defaultoption.md)
  The default option in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/mediaselectionoption(withpropertylist:))*