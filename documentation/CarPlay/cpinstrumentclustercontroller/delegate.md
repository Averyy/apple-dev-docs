# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
weak var delegate: (any CPInstrumentClusterControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<CPInstrumentClusterControllerDelegate> delegate;
```

## See Also

### Instance Properties
- [var attributedInactiveDescriptionVariants: [NSAttributedString]](./attributedinactivedescriptionvariants.md)
- [var compassSetting: CPInstrumentClusterSetting](./compasssetting.md)
- [var inactiveDescriptionVariants: [String]](./inactivedescriptionvariants.md)
- [var instrumentClusterWindow: UIWindow?](./instrumentclusterwindow.md)
- [var speedLimitSetting: CPInstrumentClusterSetting](./speedlimitsetting.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller/delegate)*