# mediaSelectionOption(withPropertyList:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVMediaSelectionOption *) mediaSelectionOptionWithPropertyList:(id) plist;
```

#### Return Value

An [`AVMediaSelectionOption`](../avmediaselectionoption.md) object containing the properites passed by `plist`. Returns `nil` when no match is found.

## Parameters

- `plist`: A property list previously obtained from an option in the group using [`propertyList()`](../avmediaselectionoption/propertylist%28%29.md) (`AVMediaSelectionOption`).

## See Also

### Accessing media selection options
- [var options: [AVMediaSelectionOption]](./options.md)
  A collection of mutually exclusive media selection options
- [var defaultOption: AVMediaSelectionOption?](./defaultoption.md)
  The default option in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/mediaselectionoption(withpropertylist:))*