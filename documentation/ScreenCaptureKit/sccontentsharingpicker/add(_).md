# add(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Adds an observer instance to notify of changes in the content-sharing picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func add(_ observer: any SCContentSharingPickerObserver)
```

```objc
- (void) addObserver:(id<SCContentSharingPickerObserver>) observer;
```

## Parameters

- `observer`: The observer instance to send notifications to.

## See Also

### Manage observers
- [func remove(any SCContentSharingPickerObserver)](./remove%28_%29.md)
  Removes an observer instance from the content-sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker/add(_:))*