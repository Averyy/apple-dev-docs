# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The object that serves as the search template’s delegate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var delegate: (any CPSearchTemplateDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CPSearchTemplateDelegate> delegate;
```

## See Also

### Providing a Search Template Delegate
- [protocol CPSearchTemplateDelegate](../cpsearchtemplatedelegate.md)
  The interface for an object that serves as the search template’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplate/delegate)*