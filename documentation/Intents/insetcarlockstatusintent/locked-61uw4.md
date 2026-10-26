# locked

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to lock the car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * locked;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * locked;
```

#### Discussion

When this property is [`true`](../../Foundation/nsexpression/true.md), lock the car; otherwise unlock the car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintent/locked-61uw4)*