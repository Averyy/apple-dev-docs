# target

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The UI control that receives pasted content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var target: (any UIPasteConfigurationSupporting)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIPasteConfigurationSupporting> target;
```

## Discussion

For example, you can assign this property a reference to a [`UITextView`](../uitextview.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipastecontrol/target)*