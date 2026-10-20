# accessibilityExpandedStatusBlock

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var accessibilityExpandedStatusBlock: (@MainActor @Sendable () -> UIAccessibility.ExpandedStatus)? { get set }
```

```objc
@property (nonatomic, copy, nullable) enum UIAccessibilityExpandedStatus (^)(void) accessibilityExpandedStatusBlock;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityexpandedstatusblock)*