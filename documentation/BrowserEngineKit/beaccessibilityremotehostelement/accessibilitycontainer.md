# accessibilityContainer

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

The remote host’s parent Accessibility element.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
weak var accessibilityContainer: AnyObject? { get set }
```

```objc
@property (nonatomic, weak) id accessibilityContainer;
```

## Discussion

Set this property to an Accessibility element’s parent view in your app’s main process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremotehostelement/accessibilitycontainer)*