# identifier

**Framework**: UIKit  
**Kind**: property

The unique identifier for this configuration object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var identifier: any NSCopying { get }
```

#### Discussion

If you did not provide an identifier when creating this object, UIKit assigns a new [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) object to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/identifier)*