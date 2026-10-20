# delegate

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the device browser.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
unowned(unsafe) var delegate: (any ICDeviceBrowserDelegate)? { get set }
```

```objc
@property (assign, nullable) id<ICDeviceBrowserDelegate> delegate;
```

## See Also

### Managing Device Browsing
- [protocol ICDeviceBrowserDelegate](../icdevicebrowserdelegate.md)
  Methods for managing the addition and removal of devices and responding to device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser/delegate)*