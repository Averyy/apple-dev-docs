# identifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name that identifies the constraint.

**Availability**:
- macOS 10.7+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/identifier)*