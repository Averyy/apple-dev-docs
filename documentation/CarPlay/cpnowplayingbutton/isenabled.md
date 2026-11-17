# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the button is enabled.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

## Discussion

When the value of this property is `true`, CarPlay draws the button with an enabled appearance and reports interactions to the handler you provided at initialization time. When the value of this property is `false`, CarPlay draws the button with a dimmed appearance and doesn’t report interactions. The default value of this property is `true`.

## See Also

### Managing the button state
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates the selected state of a custom button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbutton/isenabled)*