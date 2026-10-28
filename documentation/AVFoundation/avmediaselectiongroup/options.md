# options

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A collection of mutually exclusive media selection options

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
var options: [AVMediaSelectionOption] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMediaSelectionOption *> * options;
```

## Discussion

The value of the property is an array of [`AVMediaSelectionOption`](../avmediaselectionoption.md) objects.

## See Also

### Accessing media selection options
- [func mediaSelectionOption(withPropertyList: Any) -> AVMediaSelectionOption?](./mediaselectionoption%28withpropertylist%29.md)
  Returns the media selection options that match the given property list.
- [var defaultOption: AVMediaSelectionOption?](./defaultoption.md)
  The default option in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/options)*