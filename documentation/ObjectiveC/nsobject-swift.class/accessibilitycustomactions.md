# accessibilityCustomActions

**Framework**: Objective-C Runtime  
**Kind**: property

An array of custom actions to display along with the built-in actions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var accessibilityCustomActions: [UIAccessibilityCustomAction]? { get set }
```

#### Discussion

The array contains one or more `UIAccessibilityCustomAction` objects defining the supported actions. Assistive technologies, such as VoiceOver, display your custom actions to the user at appropriate times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitycustomactions)*