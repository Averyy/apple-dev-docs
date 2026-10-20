# delegate

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the tool picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
weak var delegate: (any PKToolPicker.Delegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PKToolPickerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/delegate-swift.property)*