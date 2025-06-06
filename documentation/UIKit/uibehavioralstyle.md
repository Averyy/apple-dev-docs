# UIBehavioralStyle

**Framework**: UIKit  
**Kind**: enum

Constants that indicate how a control behaves in apps built with Mac Catalyst.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
enum UIBehavioralStyle
```

#### Overview

If you build your app with Mac Catalyst and use the Mac idiom, you can specify the preferred behavior style for a control to change its appearance and behavior. For instance, consider an iPad app that displays a slider with a custom thumb image. By default, the Mac version of the app, built with Mac Catalyst, displays a standard macOS slider when the user interface idiom of the app is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md).

To provide a consistent appearance of the slider in the iPad and Mac versions of the app, set the [`preferredBehavioralStyle`](uislider/preferredbehavioralstyle.md) of the slider to [`UIBehavioralStyle.pad`](uibehavioralstyle/pad.md). This behavioral style tells the slider to behave as if the user interface idiom is [`UIUserInterfaceIdiom.pad`](uiuserinterfaceidiom/pad.md) even though the app uses the Mac idiom.

macOS doesn’t scale the interface of apps that use the Mac idiom, so you may need to update your app to accommodate size differences. For example, a slider with a custom thumb image may need a different image for the Mac app than the one used in the iPad app.

```swift
let slider = UISlider()
slider.minimumValue = 0
slider.maximumValue = 1
slider.value = 0.5
slider.preferredBehavioralStyle = .pad

if slider.traitCollection.userInterfaceIdiom == .mac {
    slider.setThumbImage(#imageLiteral(resourceName: "customSliderThumbMac")), for: .normal)
} else {
    slider.setThumbImage(#imageLiteral(resourceName: "customSliderThumb")), for: .normal)
}
```

To learn more about the Mac idiom, see [`Choosing a user interface idiom for your Mac app`](choosing-a-user-interface-idiom-for-your-mac-app.md).

## Topics

### Styles
- [UIBehavioralStyle.automatic](uibehavioralstyle/automatic.md)
  A style the system chooses based on the app’s targeted platform.
- [UIBehavioralStyle.pad](uibehavioralstyle/pad.md)
  A style that indicates that a control appears and behaves as it does in iPadOS.
- [UIBehavioralStyle.mac](uibehavioralstyle/mac.md)
  A style that indicates that a control appears and behaves as it does in macOS.
### Initializers
- [init?(rawValue: UInt)](uibehavioralstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var behavioralStyle: UIBehavioralStyle](uibutton/behavioralstyle.md)
  The style that determines how the button behaves.
- [var preferredBehavioralStyle: UIBehavioralStyle](uibutton/preferredbehavioralstyle.md)
  The preferred behavioral style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibehavioralstyle)*