# delegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any PKShareSecureElementPassViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PKShareSecureElementPassViewControllerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksharesecureelementpassviewcontroller/delegate)*