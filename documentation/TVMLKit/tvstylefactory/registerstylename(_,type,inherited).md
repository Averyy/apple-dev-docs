# registerStyleName(_:type:inherited:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Type Method

Creates a new style property of the indicated type.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class func registerStyleName(_ styleName: String, type: TVViewElementStyleType, inherited: Bool)
```

```objc
+ (void) registerStyle:(NSString *) styleName withType:(TVViewElementStyleType) type inherited:(BOOL) inherited;
```

## Parameters

- `styleName`: The name used to identify the style.
- `type`: The element style type as specified by [`TVViewElementStyleType`](../tvviewelementstyletype.md).
- `inherited`: Boolean indicating whether the style is able to be inherited by other styles.

## See Also

### Creating New Style Properties
- [enum TVViewElementStyleType](../tvviewelementstyletype.md)
  Describes the different style types for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvstylefactory/registerstylename(_:type:inherited:))*