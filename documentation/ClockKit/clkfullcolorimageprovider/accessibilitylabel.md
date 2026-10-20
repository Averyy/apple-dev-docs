# accessibilityLabel

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A succinct label that identifies the purpose of the image.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var accessibilityLabel: String? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSString * accessibilityLabel;
```

#### Discussion

An accessibility label should be a very short localized string that identifies the purpose of the image presented by the image provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkfullcolorimageprovider/accessibilitylabel)*