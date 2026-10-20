# delegate

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The delegate for responding to user actions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency weak var delegate: (any MarkupEditViewController.Delegate)? { get set }
```

## See Also

### Configuring the view controller
- [let supportedFeatureSet: FeatureSet](./supportedfeatureset.md)
  The supported features of this edit UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller/delegate-swift.property)*