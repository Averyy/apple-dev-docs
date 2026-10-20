# accessibilityLabel

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A localized string that describes the gague.

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

Set this property to provide a succinct description for the gauge. VoiceOver reads this property when describing the gauge. By default, this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkgaugeprovider/accessibilitylabel)*