# subbandParameters

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

An array of frequencies that describe varying sound emission across the spectrum.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var subbandParameters: [PHASEConeDirectivityModelSubbandParameters] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<PHASEConeDirectivityModelSubbandParameters *> * subbandParameters;
```

## Discussion

This property is read only. The framework sets the value to the argument you supply the [`init(subbandParameters:)`](./init%28subbandparameters%29.md) initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelparameters/subbandparameters)*