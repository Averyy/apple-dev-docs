# init(pass:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly created add-passes view controller with a single pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init?(pass: PKPass)
```

```objc
- (instancetype) initWithPass:(PKPass *) pass;
```

#### Return Value

The initialized add-passes view controller object or `nil` if there was a problem initializing the object.

## Parameters

- `pass`: The pass for the view controller to display.

## See Also

### Creating an add-passes view controller
- [init?(passes: [PKPass])](./init%28passes%29.md)
  Initializes and returns a newly created add-passes view controller with an array of passes.
- [init(issuerData: Data, signature: Data) throws](./init%28issuerdata,signature%29.md)
  Initializes and returns a new add-passes view controller with the issuer data, and signature you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/init(pass:))*