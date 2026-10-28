# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The name that identifies the constraint.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var identifier: String? { get set }
```

```objc
@property (copy, nullable) NSString * identifier;
```

## Discussion

A constraint’s identifier is available in its description. Identifiers that start with `NS` are reserved by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/identifier)*