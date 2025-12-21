# hasDisplayModeAdvanced

**Framework**: Quartz  
**Kind**: property

The property that determines whether the scanner view uses the advanced display mode.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var hasDisplayModeAdvanced: Bool { get set }
```

#### Discussion

If you create an `IKScannerDeviceView` object programmatically and want to use the advanced display mode, do the following:

- Set this property to [`true`](https://developer.apple.com/documentation/Swift/true).
- Set [`IKScannerDeviceViewDisplayMode.simple`](ikscannerdeviceviewdisplaymode/simple.md) to [`false`](https://developer.apple.com/documentation/Swift/false).
- Set [`mode`](ikscannerdeviceview/mode.md) to [`IKScannerDeviceViewDisplayMode.advanced`](ikscannerdeviceviewdisplaymode/advanced.md).

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var mode: IKScannerDeviceViewDisplayMode](ikscannerdeviceview/mode.md)
  The display mode used by the device view.
- [var hasDisplayModeSimple: Bool](ikscannerdeviceview/hasdisplaymodesimple.md)
  The property that determines whether the scanner view uses the simple display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/hasdisplaymodeadvanced)*