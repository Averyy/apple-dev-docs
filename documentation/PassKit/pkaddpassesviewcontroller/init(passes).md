# init(passes:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly created add-passes view controller with an array of passes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init?(passes: [PKPass])
```

```objc
- (instancetype) initWithPasses:(NSArray<PKPass *> *) passes;
```

#### Return Value

The initialized add-passes view controller object or `nil` if there was a problem initializing the object.

## Parameters

- `passes`: The passes for the view controller to display.

## See Also

### Creating an add-passes view controller
- [init?(pass: PKPass)](./init%28pass%29.md)
  Initializes and returns a newly created add-passes view controller with a single pass.
- [init(issuerData: Data, signature: Data) throws](./init%28issuerdata,signature%29.md)
  Initializes and returns a new add-passes view controller with the issuer data, and signature you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/init(passes:))*