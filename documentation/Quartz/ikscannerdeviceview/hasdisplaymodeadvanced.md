# hasDisplayModeAdvanced

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

The property that determines whether the scanner view uses the advanced display mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var hasDisplayModeAdvanced: Bool { get set }
```

```objc
@property BOOL hasDisplayModeAdvanced;
```

## Discussion

If you create an `IKScannerDeviceView` object programmatically and want to use the advanced display mode, do the following:

- Set this property to [`true`](../../Swift/true.md).
- Set [`IKScannerDeviceViewDisplayMode.simple`](../ikscannerdeviceviewdisplaymode/simple.md) to [`false`](../../Swift/false.md).
- Set [`mode`](./mode.md) to [`IKScannerDeviceViewDisplayMode.advanced`](../ikscannerdeviceviewdisplaymode/advanced.md).

The default value for this property is [`false`](../../Swift/false.md).

## See Also

### Setting the Device View’s Display Mode
- [var mode: IKScannerDeviceViewDisplayMode](./mode.md)
  The display mode used by the device view.
- [var hasDisplayModeSimple: Bool](./hasdisplaymodesimple.md)
  The property that determines whether the scanner view uses the simple display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/hasdisplaymodeadvanced)*