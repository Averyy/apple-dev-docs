# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The object that serves as the delegate to the list template.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

> **Deprecated**: For selection, use the handler on [`CPSelectableListItem`](../cpselectablelistitem.md) instead.

## Declaration

```swift
weak var delegate: (any CPListTemplateDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CPListTemplateDelegate> delegate;
```

## See Also

### Responding to List Events
- [protocol CPListTemplateDelegate](../cplisttemplatedelegate.md)
  The interface an object implements to serve as the delegate for a list template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/delegate)*