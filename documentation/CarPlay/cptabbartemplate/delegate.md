# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The object that acts as the template’s delegate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
weak var delegate: (any CPTabBarTemplateDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CPTabBarTemplateDelegate> delegate;
```

## Discussion

The delegate must conform to the [`CPTabBarTemplateDelegate`](../cptabbartemplatedelegate.md) protocol.

## See Also

### Managing Tab Bar Interactions
- [protocol CPTabBarTemplateDelegate](../cptabbartemplatedelegate.md)
  The methods an object implements to act as the delegate for a tab bar template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplate/delegate)*