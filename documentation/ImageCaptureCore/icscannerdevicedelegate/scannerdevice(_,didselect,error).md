# scannerDevice(_:didSelect:error:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when a functional unit is selected on the scanner.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func scannerDevice(_ scanner: ICScannerDevice, didSelect functionalUnit: ICScannerFunctionalUnit, error: (any Error)?)
```

```objc
- (void) scannerDevice:(ICScannerDevice *) scanner didSelectFunctionalUnit:(ICScannerFunctionalUnit *) functionalUnit error:(NSError *) error;
```

#### Discussion

A functional unit is selected immediately after the scanner instantiates and in response to calling [`requestSelect(_:)`](../icscannerdevice/requestselect%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevice(_:didselect:error:))*