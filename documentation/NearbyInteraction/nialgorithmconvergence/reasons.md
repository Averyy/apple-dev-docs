# reasons

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

An array of reasons that contribute to the convergence status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSString *> * reasons;
```

## Discussion

To improve the results of the framework’s Camera Assistance feature, coach the user to resolve the issues that each reason describe. For example, present text that explains what the user needs to do for each value in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergence/reasons)*