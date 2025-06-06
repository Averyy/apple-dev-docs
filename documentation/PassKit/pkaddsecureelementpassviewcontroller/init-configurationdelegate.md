# init(configuration:delegate:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a view controller using the specified pass configuration.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(configuration: PKAddSecureElementPassConfiguration, delegate: (any PKAddSecureElementPassViewControllerDelegate)?)
```

#### Discussion

The delegate must adopt the [`PKAddSecureElementPassViewControllerDelegate`](pkaddsecureelementpassviewcontrollerdelegate.md) protocol. The view controller doesn’t retain the delegate.

## Parameters

- `configuration`: The configuration that the view controller uses to create a Secure Element pass.
- `delegate`: An object that acts as the view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontroller/init(configuration:delegate:))*