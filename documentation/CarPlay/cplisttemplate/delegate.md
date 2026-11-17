# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The list template’s delegate is informed of list selection events.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
weak var delegate: (any CPListTemplateDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CPListTemplateDelegate> delegate;
```

## See Also

### Deprecated
- [protocol CPListTemplateDelegate](../cplisttemplatedelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/delegate)*