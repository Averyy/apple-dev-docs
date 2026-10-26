# displaysMessage

**Framework**: IntentsUI  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether your view controller replaces the default message interface that Siri provides.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional var displaysMessage: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL displaysMessage;
```

#### Discussion

Implement this property and return [`true`](../../Swift/true.md) when you want your view controller to display the content and recipients of a message. For example, you might return [`true`](../../Swift/true.md) when you want to provide a customized message interface. If you do not implement this property, or your implementation returns [`false`](../../Swift/false.md), Siri displays the message recipients and content using its own interface.

## See Also

### Overriding the Default Behavior
- [var displaysMap: Bool](./displaysmap.md)
  A Boolean indicating whether your view controller replaces any default map interface.
- [var displaysPaymentTransaction: Bool](./displayspaymenttransaction.md)
  A Boolean indicating whether your view controller replaces the default payment transaction interface that Siri provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuihostedviewsiriproviding/displaysmessage)*