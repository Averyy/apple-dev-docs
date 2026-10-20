# hasDisplayModeSimple

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

The property that determines whether the scanner view uses the simple display mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var hasDisplayModeSimple: Bool { get set }
```

```objc
@property BOOL hasDisplayModeSimple;
```

#### Discussion

If you create an `IKScannerDeviceView` object programmatically and want to use the simple display mode, do the following:

- Set this property to [`true`](../../Swift/true.md).
- Set [`IKScannerDeviceViewDisplayMode.advanced`](../ikscannerdeviceviewdisplaymode/advanced.md) to [`false`](../../Swift/false.md).
- Set [`mode`](./mode.md) to [`IKScannerDeviceViewDisplayMode.simple`](../ikscannerdeviceviewdisplaymode/simple.md).

The default value for this property is [`false`](../../Swift/false.md).

## See Also

### Setting the Device View’s Display Mode
- [var mode: IKScannerDeviceViewDisplayMode](./mode.md)
  The display mode used by the device view.
- [var hasDisplayModeAdvanced: Bool](./hasdisplaymodeadvanced.md)
  The property that determines whether the scanner view uses the advanced display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/hasdisplaymodesimple)*