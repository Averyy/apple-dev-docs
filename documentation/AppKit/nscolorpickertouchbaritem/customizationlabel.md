# customizationLabel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The user-visible string identifying this item during touch bar customization.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var customizationLabel: String! { get set }
```

```objc
@property (copy, readwrite, null_resettable) NSString * customizationLabel;
```

## Discussion

The default value of this property is the localized version of “Color Picker”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/customizationlabel)*