# propertyList()

**Framework**: AVFoundation  
**Kind**: method

Returns a serializable property list that’s sufficient to identify the option within its group.

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
func propertyList() -> Any
```

#### Return Value

A serializable property list that you can use to obtain an instance of [`AVMediaSelectionOption`](avmediaselectionoption.md) representing the same option as the receiver using [`mediaSelectionOption(withPropertyList:)`](avmediaselectiongroup/mediaselectionoption(withpropertylist:).md).

#### Discussion

You can serialize the returned property list using [`PropertyListSerialization`](https://developer.apple.com/documentation/Foundation/PropertyListSerialization).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/propertylist())*