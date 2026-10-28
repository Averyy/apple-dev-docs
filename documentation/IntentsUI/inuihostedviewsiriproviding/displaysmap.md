# displaysMap

**Framework**: IntentsUI  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether your view controller replaces any default map interface.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional var displaysMap: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL displaysMap;
```

## Mentions

- [Configuring the View Controller for Your Custom Interface](../../SiriKit/configuring-the-view-controller-for-your-custom-interface.md)

## Discussion

Implement this property and return [`true`](../../Swift/true.md) when you want your view controller to provide the map showing location-related information. If you do not implement this property, or your implementation returns [`false`](../../Swift/false.md), Siri displays its own map in addition to the content that you provide.

## See Also

### Overriding the Default Behavior
- [var displaysMessage: Bool](./displaysmessage.md)
  A Boolean indicating whether your view controller replaces the default message interface that Siri provides.
- [var displaysPaymentTransaction: Bool](./displayspaymenttransaction.md)
  A Boolean indicating whether your view controller replaces the default payment transaction interface that Siri provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuihostedviewsiriproviding/displaysmap)*