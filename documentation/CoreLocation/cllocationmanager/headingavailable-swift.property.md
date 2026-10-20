# headingAvailable

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the location manager is able to generate heading-related events.

**Availability**:
- iOS 3.0+ - Deprecated in 4.0
- iPadOS 3.0+ - Deprecated in 4.0
- Mac Catalyst 3.0+ - Deprecated in 4.0
- macOS 10.15+ - Deprecated in 10.15
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`headingAvailable()`](./headingavailable%28%29.md) class method instead.

## Declaration

```swift
var headingAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL headingAvailable;
```

#### Discussion

Heading data may not be available on all iOS-based devices. You should check the value of this property before asking the location manager to deliver heading-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/headingavailable-swift.property)*