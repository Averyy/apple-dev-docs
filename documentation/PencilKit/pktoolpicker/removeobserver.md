# removeObserver(_:)

**Framework**: PencilKit  
**Kind**: method

Removes the specified object from the list of objects to notify when the picker configuration changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func removeObserver(_ observer: any PKToolPickerObserver)
```

## Parameters

- `observer`: The object to stop sending notifications to.

## See Also

- [func addObserver(any PKToolPickerObserver)](pktoolpicker/addobserver(_:).md)
  Adds the specified object to the list of objects to notify when the picker configuration changes.
- [protocol PKToolPickerObserver](pktoolpickerobserver.md)
  An interface you use to detect when the user changes the selected tools and drawing characteristics of a tool picker object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/removeobserver(_:))*