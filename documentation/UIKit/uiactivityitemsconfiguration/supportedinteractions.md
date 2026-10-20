# supportedInteractions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The types of interactions that the configuration supports.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var supportedInteractions: [UIActivityItemsConfigurationInteraction] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * supportedInteractions;
```

#### Discussion

The default value is all known interactions.

## See Also

### Managing supported interactions
- [struct UIActivityItemsConfigurationInteraction](../uiactivityitemsconfigurationinteraction.md)
  A structure that describes types of interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/supportedinteractions)*