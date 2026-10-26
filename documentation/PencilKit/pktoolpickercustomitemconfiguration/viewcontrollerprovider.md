# viewControllerProvider

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

A closure to provide a view controller above the system controls in the tool attributes popover.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) UIViewController * (^viewControllerProvider)(PKToolPickerCustomItem *toolPickerItem);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitemconfiguration/viewcontrollerprovider)*