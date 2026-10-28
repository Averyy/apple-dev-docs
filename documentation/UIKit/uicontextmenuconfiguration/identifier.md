# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for this configuration object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: any NSCopying { get }
```

```objc
@property (nonatomic, readonly) id<NSCopying> identifier;
```

## Discussion

If you did not provide an identifier when creating this object, UIKit assigns a new [`UUID`](../../Foundation/uuid.md) object to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/identifier)*