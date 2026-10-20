# delegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A delegate object that receives messages about the changes to the Apple Pay Later view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```swift
unowned(unsafe) var delegate: any PKPayLaterViewDelegate { get set }
```

```objc
@property (nonatomic, assign) id<PKPayLaterViewDelegate> delegate;
```

## See Also

### Responding to changes in the view’s height
- [protocol PKPayLaterViewDelegate](../pkpaylaterviewdelegate.md)
  Methods the framework calls when the Apple Pay Later view’s size changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview/delegate)*