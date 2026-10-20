# addObserver(_:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified object to the list of objects to notify when the picker configuration changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addObserver(_ observer: any PKToolPickerObserver)
```

```objc
- (void) addObserver:(id<PKToolPickerObserver>) observer;
```

## Parameters

- `observer`: The object to notify when changes occur.

## See Also

### Detecting changes to the picker
- [func removeObserver(any PKToolPickerObserver)](./removeobserver%28_%29.md)
  Removes the specified object from the list of objects to notify when the picker configuration changes.
- [protocol PKToolPickerObserver](../pktoolpickerobserver.md)
  An interface you use to detect when the user changes the selected tools and drawing characteristics of a tool picker object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/addobserver(_:))*